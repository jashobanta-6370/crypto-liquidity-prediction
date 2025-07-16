# 🪙 Cryptocurrency Liquidity Prediction

This project predicts the **liquidity index** of cryptocurrencies based on real-time trading metrics using a trained machine learning model.

Built with:
- 🧠 **Python + scikit-learn**
- 🌐 **Flask Web App**
- 📊 **Random Forest Regressor**
- 💻 Designed for deployment (e.g., Render, local hosting)

---
## 📸 Live Project Link  
🔗 [Click to Open Web App](https://crypto-liquidity-prediction-production.up.railway.app/)

---

## 📊 Exploratory Data Analysis (EDA) REPORTS

### 🔹 Figure 1: Correlation Heatmap

Shows correlations between price, market cap, volume, volatility, and liquidity index.

<img width="844" height="614" alt="download" src="https://github.com/user-attachments/assets/4d58ab88-e6c0-485a-9f28-3d9a9666a2d7" />


---

### 🔹 Figure 2: Price Distribution

Histogram of all cryptocurrency prices in the dataset.

<img width="704" height="470" alt="download (1)" src="https://github.com/user-attachments/assets/9135eeb8-ac02-4102-abeb-8db9b7fcb7a0" />

---

### 🔹 Figure 3: Liquidity Index Distribution

Histogram of the calculated liquidity index across all coins.

<img width="704" height="470" alt="download (2)" src="https://github.com/user-attachments/assets/095760ea-657e-4a8e-a720-6c24989b62c6" />

---

### 🔹 Figure 4: Market Cap vs Price

Scatter plot illustrating the relationship between market cap and price.


<img width="713" height="470" alt="download (3)" src="https://github.com/user-attachments/assets/c00f01a6-2a53-43fd-abc4-b3dcdf6ae473" />

---

### 🔹 Figure 5: Top 10 Coins by Average Liquidity Index

Coins like Tether, USD Coin, and DAI show the highest average liquidity.

<img width="915" height="547" alt="download (4)" src="https://github.com/user-attachments/assets/47b9d8ff-0b7d-4161-93d5-015e29188b4e" />

---



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
