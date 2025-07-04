# 💻 Laptop Price Prediction

A machine learning web app that predicts the price of a laptop based on its specifications — including brand, processor, RAM, storage, GPU, OS, screen resolution, and more.

Built using Python, Pandas, Scikit-learn, and Streamlit.

---

## 📸 Demo

![Screenshot 2025-07-04 131215](https://github.com/user-attachments/assets/20fa6e3a-3dab-4cab-8d90-136447b35f82)
)
![Screenshot 2025-07-04 131231](https://github.com/user-attachments/assets/d0903633-9bfd-4e9f-adb3-ae9165f0c41e)
)
![Screenshot 2025-07-04 131239](https://github.com/user-attachments/assets/94cc714b-5f43-4fba-a5fb-a7ab587d2977)
)
> *(Adding  a screenshot  of the app here)*

-----------------

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
