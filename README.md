# 📊 Fake News Detection 🚨

## 🔍 Project Overview

Welcome to the **Fake News Detection** web application! This app allows users to input either a **news URL** or **raw text**, and the system will analyze the content to determine whether it is **fake** or **legitimate**. The app uses a **logistic regression model** trained on a labeled dataset containing both fake and real news to make its predictions.

With an impressive **accuracy of 99.01%**, this project is a great demonstration of the power of machine learning for natural language processing (NLP) tasks.

---

## 🤖 Model Overview

The project uses a **logistic regression model** trained on a dataset with both **fake** and **real** news content. It processes the text and provides predictions about the authenticity of the news. This model is persisted using **joblib** for seamless integration with the **Flask app**.

---

## 🌟 Features

- **URL Analysis**: Paste any URL, and the system will fetch the content and analyze its authenticity.
- **Text Analysis**: Paste raw news text, and get real-time classification.
- **Result Display**: View whether the news is fake or real with confidence scores.
- **Real-time Predictions**: Receive results instantly using Flask APIs.
- **Error Handling**: Invalid inputs or errors are handled with appropriate messages.

---

## 🛠 Installation and Setup

### Step 1: Create a Virtual Environment

1. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Step 2: Install Dependencies

After activating the virtual environment, install all the required libraries listed in `requirements.txt`.

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---


## 📂 Project Structure

```plaintext
fake-news-detection/
│
├── app.py                   # Main Flask application
├── model/
│   ├── logreg_model.pkl     # Saved machine learning model
│   ├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
├── templates/
│   ├── index.html           # HTML template for the web interface
│   ├── script.js            # Custom JavaScript for dynamic behavior
├── requirements.txt         # List of dependencies
├── train_model.py           # Script to train the model
└── README.md                # Project description
```

### File Descriptions:
- **`app.py`**: The main Flask application that handles routing and serving the model for predictions.
- **`model/`**: Contains the trained machine learning model (`logreg_model.pkl`) and the TF-IDF vectorizer (`tfidf_vectorizer.pkl`) used for text vectorization.
- **`templates/`**: Stores the HTML and JavaScript files that power the front-end of the app.
  - **`index.html`**: The main HTML interface where users input text or URLs for analysis.
  - **`script.js`**: JavaScript for dynamic behavior and AJAX requests to the backend.
- **`requirements.txt`**: Contains a list of all the dependencies required to run the project.
- **`train_model.py`**: A script used to train the logistic regression model using labeled datasets. After training, the model is saved for use in `app.py`.
- **`README.md`**: The project documentation providing details about the app, setup, and how to use it.


---

## 📚 Libraries and Dependencies

The following libraries are used in the project:

- **Flask** (⚡) - A micro web framework to serve the model and handle HTTP requests.
- **Flask-CORS** (🌐) - Handles Cross-Origin Resource Sharing (CORS) for API requests.
- **Flask-Limiter** (⏱️) - Provides rate limiting to prevent API abuse.
- **Flasgger** (📜) - Automatically generates API documentation from the code.
- **Flask-CacheControl** (🗄️) - Caching for API responses to improve performance.
- **Pandas** (📊) - Data manipulation library used to handle the dataset.
- **Numpy** (🔢) - Used for numerical computations and working with arrays.
- **Scikit-learn** (📈) - A machine learning library used for training and evaluating models.
- **Joblib** (💾) - Saves the trained machine learning model for future predictions.
- **BeautifulSoup4** (🔍) - Used for web scraping to analyze content from URLs (if implemented).
- **Requests** (🌐) - A simple HTTP library for making requests to external resources.
- **Imblearn** (⚖️) - Used for handling class imbalance via SMOTE (Synthetic Minority Over-sampling Technique).

---

## 🚀 How to Run the Application

1. **Activate the Virtual Environment:**

   ```bash
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate   # Windows
   ```

2. **Run the Flask Application:**

   ```bash
   python app.py
   ```

   The application will be hosted at `http://127.0.0.1:5000/`. Open this URL in your browser to interact with the web interface.

---

## 🌐 API Endpoints

- **POST `/predict`**: Accepts a `text` parameter for text-based analysis.
- **POST `/analyze`**: Accepts a `url` parameter for URL-based analysis.

Both endpoints return a JSON response with the prediction and confidence score.

---

## 📋 Requirements File (`requirements.txt`)

The `requirements.txt` file includes all necessary libraries:

```plaintext
flask==3.0.2            # Flask web framework
flask-cors==4.0.0       # CORS handling
flask-limiter==3.5.0    # API rate limiting
flasgger==0.9.5         # API documentation
flask-cachecontrol==0.3.0 # Cache control for Flask
pandas==2.0.3           # Data manipulation
scikit-learn==1.3.0     # Machine learning model library
joblib==1.3.2           # Model persistence
beautifulsoup4==4.12.3  # Web scraping for URL analysis
requests==2.31.0        # HTTP requests library
numpy==1.24.3           # Numerical computation
imblearn==0.11.0        # Class imbalance handling (SMOTE)
```

---

## 🎯 Accuracy

The model achieved an impressive **99.01%** accuracy on the test set, which indicates its high performance in classifying news articles accurately.

### Accuracy Screenshot

![Accuracy Screenshot](screenshots/accuracy_screenshot.png)

---

## 🎥 Demo Video

Check out the **demo video** that shows how the Fake News Detection app works in real-time.


https://github.com/user-attachments/assets/7a3228c5-1a10-430a-8187-86092f8ea490


---

## 📸 Output Screenshots

### 1. **Sample Text Analysis Output**

![Text Analysis Output](screenshots/text_analysis_output1.png)
![Text Analysis Output](screenshots/text_analysis_output.png)

### 2. **Sample URL Analysis Output**

![URL Analysis Output](screenshots/url_analysis_output1.png)
![URL Analysis Output](screenshots/url_analysis_output.png)

### 3. **Dynamic View on Small Screen**

![Small Screen View](screenshots/small_screen_output.png)


---

## 🛠 Contributing

Feel free to fork this repository and submit pull requests. Contributions to improve the model or enhance the app are highly welcome! If you find any issues or have suggestions, please open an issue in the repository.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 **Contact & Support**
Got questions or suggestions? Reach out! 😊
- GitHub: [officialayushyadav15](https://github.com/officialayushyadav15)

