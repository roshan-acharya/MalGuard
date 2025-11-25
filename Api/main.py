from flask import Flask, request, jsonify
from flask_cors import CORS
from pipeline.predict import predict_url

app = Flask(__name__)
CORS(app)


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
        prediction = predict_url(url, './models/one_class_svm_model.pkl')
        result = "Phishing" if prediction == -1 else "Legitimate"

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
