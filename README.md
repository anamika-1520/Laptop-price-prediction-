# 💻 Laptop Price Prediction

A machine‑learning web app that predicts a laptop’s price from its specifications—brand, CPU, RAM, storage, GPU, display, and more—built with Python, Pandas, Scikit‑learn, and Streamlit.

---

## 🎬 Demo Video

<p align="center">
  <!-- Option 1: link to a YouTube video with a thumbnail -->
  <a href="https://youtu.be/YOUR_VIDEO_ID" target="_blank">
    <img src="images/video_thumbnail.png" alt="Watch the demo" width="80%">
  </a>
  <!-- If you prefer to embed an MP4 that you committed to the repo, comment the link above and
       uncomment the <video> tag below.  GitHub will render it inline on most browsers. -->
  <!--
  <video src="demo.mp4" controls style="width:100%;max-width:800px;border-radius:12px;"></video>
  -->
</p>

> **Tip:**  
> 1. Record with OBS or ScreenToGif ➜ export MP4 (or GIF).  
> 2. Create a small thumbnail PNG (e.g., 1280 × 720).  
> 3. Commit `demo.mp4` (or upload to YouTube) and `images/video_thumbnail.png`.  
> 4. Update the link / filename above.

---

## 🚀 Features

- 🔍 **Instant price prediction** from user‑entered specs  
- 🧠 Multiple ML models compared (Linear, Ridge, Random Forest, SVR)  
- ⚙️ **Full preprocessing pipeline**: encoding, scaling, log‑transform  
- 📈 Metrics page with RMSE and R² charts  
- 🖥️ Clean Streamlit UI; responsive on desktop and mobile

---

## 🗂 Dataset

| Field            | Type      | Example              |
|------------------|-----------|----------------------|
| Brand            | Categorical | Dell |
| Processor        | Categorical | Intel i5‑1135G7 |
| RAM (GB)         | Numeric   | 8 |
| Storage (GB)     | Numeric   | 512 |
| GPU              | Categorical | NVIDIA MX350 |
| Screen Size (″)  | Numeric   | 14 |
| Resolution       | Categorical | 1920×1080 |
| Weight (kg)      | Numeric   | 1.4 |
| Touchscreen      | Binary    | 0 / 1 |
| **Price (₹)**    | Target    | 62 990 |

Source: **YOUR‑DATASET‑SOURCE** (e.g., custom Flipkart scrape or Kaggle).

---

## 🛠 Tech Stack

- Python 3.11, Pandas, NumPy  
- Scikit‑learn, Matplotlib  
- Streamlit (frontend)  
- joblib (model persistence)

---

## 🔧 Installation

```bash
# Clone
git clone https://github.com/YOUR‑USERNAME/laptop-price-predictor.git
cd laptop-price-predictor

# (Optional) create & activate venv
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Run the app
streamlit run app.py
