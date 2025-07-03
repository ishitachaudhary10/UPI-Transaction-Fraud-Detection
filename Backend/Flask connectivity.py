!pip install flask-cors
!pip install flask
!pip install pyngrok
from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok, conf
import pandas as pd
import numpy as np

# 1. Ngrok Auth
conf.get_default().auth_token = "" #add your-ngrok-authtoken (dont share yours on github)

# 2. Flask App + CORS
app = Flask(__name__)
CORS(app)  # ✅ This line is required!


# 3. Start Ngrok Tunnel
public_url = ngrok.connect(5000)
print("🌐 Public URL:", public_url)

# 4. Your ML code should already define: model, scaler, features

@app.route("/")
def home():
    return "UPI Fraud API Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = np.array([[
        data['amount'],
        data['sender_age'],
        data['receiver_age'],
        data['hour_of_day'],
        data['is_weekend'],
        data['transaction_hour'],
        data['transaction_day']
    ]])
    input_df = pd.DataFrame(input_data, columns=features)
    scaled = scaler.transform(input_df)
    prediction = model.predict(scaled)
    return jsonify({
        "prediction": "Fraud" if prediction[0] == -1 else "Normal"
    })

app.run(port=5000)
