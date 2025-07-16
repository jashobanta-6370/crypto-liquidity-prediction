from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model/liquidity_model.joblib')
scaler = joblib.load('model/scaler.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from form
        price = float(request.form['price'])
        h1 = float(request.form['h1'])
        h24 = float(request.form['h24'])
        d7 = float(request.form['d7'])
        volume = float(request.form['volume'])
        market_cap = float(request.form['market_cap'])
        volatility = float(request.form['volatility'])

        # Create input array and scale it
        input_data = np.array([[price, h1, h24, d7, volume, market_cap, volatility]])
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]

        return render_template('index.html', prediction_text=f"Predicted Liquidity Index: {prediction:.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run()
