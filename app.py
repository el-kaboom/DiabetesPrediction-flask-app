from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

CORS(app)

# Load the saved model and scaler
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict_diabetes():
    try:
        data = request.get_json()

        required_fields = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DPF', 'Age']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing fields'}), 400

        features = np.array([[data['Pregnancies'], data['Glucose'], data['BloodPressure'],
                              data['SkinThickness'], data['Insulin'], data['BMI'], data['DPF'], data['Age']]])

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)[0]

        if prediction:
            return jsonify({'prediction': 'Diabetes detected'}), 200
        else:
            return jsonify({'prediction': 'No diabetes'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)