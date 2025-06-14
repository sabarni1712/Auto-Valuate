# 🚗 AutoValuate: Used Car Price Predictor

**AutoValuate** is a machine learning–powered web application that predicts the fair market price of a used car based on its specifications. It helps buyers and sellers in the second-hand car market make informed, data-driven pricing decisions using a simple web interface.

---

## 📌 Features

- 🎯 Accurate price prediction for used cars
- 🧠 Machine learning model (Linear Regression)
- 🌐 Streamlit-based interactive web UI
- 💡 Real-time output based on user inputs
- ⚡ Fast and lightweight for local or cloud deployment

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Frontend:** Streamlit
- **Backend:** Scikit-learn (ML model)
- **Libraries Used:**
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `streamlit`
  - `pickle` / `joblib`

---

## 🚀 Installation & Usage

### 🔧 Prerequisites
- Python 3.8 or higher
- `pip` package manager

### 🧪 Installation
```bash
git clone https://github.com/yourusername/used-car-price-predictor.git
cd used-car-price-predictor
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
streamlit run app.py
```

- 🌐 Open your browser and visit: [http://localhost:8501](http://localhost:8501)
- 💡 Use the form to input car details and get a predicted selling price instantly

---

## 📊 Model Details

- **🧠 Algorithm Used:** Linear Regression
- **📂 Training Data:** Scraped from [Quikr.com](https://www.quikr.com/cars)
- **🧹 Preprocessing:**
  - One-hot encoding of categorical variables
  - Scaling of numeric values (e.g., kilometers driven)
- **📈 Evaluation Metrics:**
  - R² Score
  - Mean Absolute Error (MAE)

---

## 🖼️ Demo



---

## 🔮 Future Scope

- 🤖 Integrate advanced models like XGBoost, Random Forest
- 🖼️ Use CNNs for image-based condition analysis
- ☁️ Add user login, dashboards, and cloud storage
- 📱 Create a mobile app for wider access

---

## 📚 References

- 📘 [Pandas](https://pandas.pydata.org/)
- 🤖 [Scikit-learn](https://scikit-learn.org/)
- 🌐 [Streamlit](https://streamlit.io/)
- 📊 Dataset Source: [Quikr.com](https://www.quikr.com/cars)

---












