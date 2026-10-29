from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("diabetes_model.pkl")

@app.route("/")
def home():
    return "Diabetes Progression Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = model.predict([data["features"]])

    return jsonify({
        "prediction": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=False, port=5000)