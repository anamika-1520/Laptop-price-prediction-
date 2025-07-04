# 💻 Laptop Price Prediction

A machine learning web app that predicts the price of a laptop based on its specifications — including brand, processor, RAM, storage, GPU, OS, screen resolution, and more.

Built using Python, Pandas, Scikit-learn, and Streamlit.

---

## 📸 Demo

![App Screenshot](images/demo.png)

> *(Add a screenshot or demo GIF of the app here)*

---

## 🚀 Features

- 🔍 Predict laptop price from user input specs
- 🧠 Multiple ML models implemented and compared:
  - Linear Regression
  - Ridge Regression
  - Random Forest Regressor
  - Support Vector Regressor (SVR)
- 📈 Model evaluation with RMSE and R² Score
- ⚙️ Streamlit app for easy use
- ✅ Preprocessing pipeline: encoding + scaling + transformation

---

## 🧾 Dataset Used

- **Source**: Custom-collected dataset / Kaggle / Flipkart scraped data *(specify your source)*  
- **Attributes**:
  - Brand
  - Processor (CPU)
  - RAM (GB)
  - Storage (SSD/HDD)
  - GPU
  - Operating System
  - Screen Size & Resolution
  - Weight
  - Touchscreen (Yes/No)
  - Price (Target Variable)

---

## 🛠️ Tech Stack

- Python 3.11
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib, Seaborn

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor

# 2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
