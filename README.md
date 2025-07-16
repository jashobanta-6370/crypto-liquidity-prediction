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

![Web UI](<img width="1696" height="765" alt="Screenshot 2025-07-16 150636" src="https://github.com/user-attachments/assets/0c21f889-8a45-4f92-b34d-61e2e4b7ff39" />
)

### 🔹 Screenshot 2 – Model Evaluation or Result

![Prediction](<img width="1639" height="489" alt="Screenshot 2025-07-16 150651" src="https://github.com/user-attachments/assets/086be693-e8d0-4baf-9636-3166cb59f794" />
)

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
