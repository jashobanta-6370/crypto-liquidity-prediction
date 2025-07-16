# 🪙 Cryptocurrency Liquidity Prediction

This project predicts the **liquidity index** of cryptocurrencies based on real-time trading metrics using a trained machine learning model.

Built with:
- 🧠 **Python + scikit-learn**
- 🌐 **Flask Web App**
- 📊 **Random Forest Regressor**
- 💻 Designed for deployment (e.g., Render, local hosting)

---

## 📸 Project Preview

> Replace the links below with your image file paths (e.g., `/images/demo.png` or direct GitHub raw links)

### 🔹 Screenshot 1 – Web App Interface
<img width="1696" height="765" alt="Screenshot 2025-07-16 150636" src="https://github.com/user-attachments/assets/6c23ca3a-93ce-4fa9-932f-440106dcb90e" />

### 🔹 Screenshot 2 – Model  Result

<img width="1639" height="489" alt="Screenshot 2025-07-16 150651" src="https://github.com/user-attachments/assets/f380b3cc-9ca4-4a9e-8e30-b0aa64bab5aa" />

---

## 🧠 Features & Workflow

- Input metrics: `price`, `volume`, `market cap`, `% changes`, `volatility`
- Feature engineering: `liquidity_index = (volume / market_cap) / volatility`
- Model: `RandomForestRegressor` (trained on CoinGecko data)
- Output: Predicts a continuous **liquidity score**
- Frontend: Responsive HTML with Bootstrap styling

---

## 🛠️ How to Run Locally

### 🔹 1. Clone the Repo

```bash
git clone https://github.com/jashobanta-6370/crypto-liquidity-prediction.git
cd crypto-liquidity-prediction
