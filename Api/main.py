from flask import Flask, request, jsonify
from flask_cors import CORS
from pipeline.predict import predict_url
import pandas as pd
from urllib.parse import * 

app = Flask(__name__)
CORS(app)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

safe=pd.read_csv(BASE_DIR / 'Data/safe_links.csv')

@app.route("/")
def home():
    return {"message": "PhishGuard Flask API Working "}

# Prediction Endpoint
@app.route("/predict", methods=["GET"])
def predict():
    url = request.args.get("url")  #Extrct URL from query parameter

    if not url:
        return jsonify({"error": "Missing ?url= parameter"}), 400

    try:
        print("Predicting for URL:", url)
        parse_url = urlparse(url)
        domain = parse_url.hostname
        scheme= parse_url.scheme
        combine= scheme + "://" + domain
        if combine in safe['url'].values:
            return jsonify({
                "url": url,
                "prediction": "Legitimate",
                "raw_value": 1
            })
        else:
            prediction = predict_url(url, BASE_DIR / 'models/one_class_svm_model.pkl')
            result = "Phishing" if prediction == -1 else "Legitimate"
            print(prediction)
            return jsonify({
                "url": url,
                "prediction": result,
                "raw_value": int(prediction)
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Server
if __name__ == "__main__":
    app.run(debug=True)
