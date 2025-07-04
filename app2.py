import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Sample inputs (replace these with your Streamlit inputs)
st.title("Laptop Price Predictor")
# open files
pipe=pickle.load(open("pipe.pkl",'rb'))
df=pickle.load(open('df.pkl','rb'))
company = st.selectbox("Brand", ["Dell", "HP", "Apple"])  # example
type = st.selectbox("Type", ["Ultrabook", "Gaming", "Notebook"])
ram = st.selectbox("RAM (in GB)", [4, 8, 16])
weight = st.number_input("Weight (kg)")
touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])
ips = st.selectbox("IPS Display", ["Yes", "No"])
screen_size = st.number_input("Screen Size (inches)")
resolution = st.selectbox("Screen Resolution", ["1920x1080", "1366x768", "1600x900"])
cpu = st.selectbox("CPU", ["Intel Core i7", "Intel Core i5", "AMD Ryzen"])
hdd = st.selectbox("HDD (GB)", [0, 500, 1000])
ssd = st.selectbox("SSD (GB)", [0, 256, 512])
gpu = st.selectbox("GPU", ["Nvidia GTX 1650", "Intel HD", "AMD Radeon"])
os = st.selectbox("Operating System", ["Windows", "Mac", "Linux"])

# Convert resolution to x_res and y_res
x_res = int(resolution.split('x')[0])
y_res = int(resolution.split('x')[1])
ppi = ((x_res**2 + y_res**2) ** 0.5) / screen_size

# Convert 'Yes'/'No' to 1/0
touchscreen = 1 if touchscreen == "Yes" else 0
ips = 1 if ips == "Yes" else 0

# Create input as a DataFrame
query = pd.DataFrame([[company, type, ram, weight, touchscreen, ips, ppi,
                       cpu, hdd, ssd, gpu, os]],
    columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips', 'Ppi',
             'Cpu', 'Hdd', 'Ssd', 'Gpu', 'Os'])

# Predict
prediction = np.exp(pipe.predict(query)[0])

# Display
st.title("The Predicted Price of this configuration is ₹" + str(int(prediction)))
