from flask import Flask, request, jsonify
from flask_cors import CORS
from pipeline.predict import predict_url
import pandas as pd
from urllib.parse import * 
import os

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
    print("Predicting for URL:", url)
    parse_url = urlparse(url)
    domain = parse_url.hostname
    scheme= parse_url.scheme
    domain_norm = domain.lower().replace("www.", "")
    combine= scheme + "://" + domain_norm
      

    if not url:
        return jsonify({"error": "Missing ?url= parameter"}), 400

    try:
        if combine in safe['url'].values:
            return jsonify({
                "url": domain,
                "prediction": "Legitimate",
                "raw_value": 1
            })
        else:
            prediction = predict_url(url, BASE_DIR / 'models/model.pkl')
            result = "Malicious" if prediction == -1 else "Legitimate"
            print(prediction)
            return jsonify({
                "url": domain,
                "prediction": result,
                "raw_value": int(prediction)
            })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
