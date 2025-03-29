from flask import Flask, request, jsonify, render_template
import joblib
import os
import logging

app = Flask(__name__)

# Load your trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'logreg_model.pkl')
vectorizer_PATH = os.path.join(os.path.dirname(__file__), 'tfidf_vectorizer.pkl')

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(vectorizer_PATH)
    print("✅ Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Serve the HTML template for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# URL analysis endpoint (optional for future)
@app.route('/analyze', methods=['POST'])
def analyze_url():
    try:
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({'error': 'No URL provided'}), 400

        # Add URL analysis logic here if needed
        # Placeholder response for now
        return jsonify({'result': 'URL analysis is coming soon!'})

    except Exception as e:
        logging.error(f"URL analysis failed: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

# Prediction endpoint for news classification
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        news_text = data.get('text')

        if not news_text:
            return jsonify({'error': 'No text provided'}), 400

        logging.info(f"Received text for prediction: {news_text}")

        # Vectorize and predict
        text_vectorized = vectorizer.transform([news_text])
        prediction = model.predict(text_vectorized)[0]

        # Corrected result format
        result = 'Real' if prediction == 1 else 'Fake'
        is_fake = True if result == 'Fake' else False

        logging.info(f"Prediction result: {result}")

        # Return updated result format
        return jsonify({'isFake': is_fake, 'details': f'Prediction: {result}'})

    except Exception as e:
        logging.error(f"Prediction failed: {str(e)}")
        return jsonify({'error': 'Internal Server Error. Please try again later.'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
