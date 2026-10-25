import pandas as pd
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pre-trained pipeline/model
model = joblib.load("best_model.pkl")

@app.route("/", methods=["GET"])
def home():
    return "SuperKart Sales Forecasting API is running."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve payload data
        data = request.get_json(force=True)

        # Convert payload into DataFrame
        if isinstance(data, dict):
            df_input = pd.DataFrame([data])
        elif isinstance(data, list):
            df_input = pd.DataFrame(data)
        else:
            return jsonify({"error": "Invalid input format. Must be a JSON object or array."}), 400

        # Generate predictions
        predictions = model.predict(df_input)

        # Return predictions as a JSON response
        return jsonify({"predictions": predictions.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
