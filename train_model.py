import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import re
import string
import os

# Configuration
MIN_WORDS = 50
REP_THRESHOLD = 0.3

def load_data(file_path):
    """Robust data loader with multiple fallback strategies"""
    try:
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(
            file_path,
            engine="python",
            encoding="utf-8",
            on_bad_lines="skip",
            quotechar='"',
            delimiter=",",
        )
        if df.empty:
            raise ValueError(f"{file_path} is empty or not loaded properly.")
        return df
    except Exception as e:
        try:
            return pd.read_csv(
                file_path, sep="\t", engine="python", encoding="latin-1", on_bad_lines="skip"
            )
        except Exception as e:
            try:
                with open(file_path, "r", encoding="latin-1") as f:
                    return pd.DataFrame(
                        {"text": [line.strip() for line in f if line.strip()]}
                    )
            except Exception as e:
                print(f"Failed to load {file_path}: {str(e)}")
                return pd.DataFrame()


def clean_text(text):
    """Advanced text cleaning function"""
    text = re.sub(r"\[.*?\]", "", str(text))  # Remove text inside []
    text = re.sub(r"https?://\S+|www\.\S+", "", text)  # Remove URLs
    text = re.sub(r"<.*?>+", "", text)  # Remove HTML tags
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # Remove punctuation
    text = re.sub(r"\n", " ", text)  # Remove line breaks
    text = re.sub(r"\w*\d\w*", "", text)  # Remove words with numbers
    text = re.sub(r"\s{2,}", " ", text)  # Remove multiple spaces
    return text.lower().strip()


def check_repetition(text):
    """Calculate text uniqueness ratio"""
    sentences = [s.strip() for s in re.split(r"[.!?]", text) if s.strip()]
    if len(sentences) < 2:
        return 1.0  # Not enough sentences to check repetition
    unique = len(set(sentences))
    return unique / len(sentences)


# Load and clean data
print("Loading and preprocessing data...")
data_fake = load_data("Fake.csv")
data_true = load_data("True.csv")

# Debug if files loaded successfully
if data_fake.empty or data_true.empty:
    print("Error: One or both datasets could not be loaded.")
    exit(1)

# Assign labels to datasets
data_fake["class"] = 0  # Fake news class
data_true["class"] = 1  # Real news class

# Check for the correct text column or fallback to first column
if "text" not in data_fake.columns:
    data_fake["text"] = data_fake.iloc[:, 0]
if "text" not in data_true.columns:
    data_true["text"] = data_true.iloc[:, 0]

# Merge datasets and shuffle
data = pd.concat([data_fake[["text", "class"]], data_true[["text", "class"]]], axis=0)
data = data.sample(frac=1).reset_index(drop=True)

# Clean text
print("Cleaning text data...")
data["text"] = data["text"].apply(clean_text)

# Debug: Print sample data to verify
print(data.head())

# Check for empty rows after cleaning
data = data[data["text"].str.strip() != ""]

if data.empty:
    print("Error: Data is empty after cleaning.")
    exit(1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    data["text"], data["class"], test_size=0.25, random_state=42
)

# Vectorization
print("Creating TF-IDF vectorizer...")
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Check vectorizer output
if X_train_vec.shape[0] == 0 or X_test_vec.shape[0] == 0:
    print("Error: Vectorization resulted in empty data. Check input.")
    exit(1)

# Model training
print("Training Logistic Regression...")
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_train_vec, y_train)

# Model accuracy
accuracy = model.score(X_test_vec, y_test)
print(f"Validation Accuracy: {accuracy:.2%}")

# Save model and vectorizer
print("Saving model and vectorizer...")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(model, "logreg_model.pkl")
print("Model and vectorizer saved successfully!")
