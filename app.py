import pickle
import numpy as np
import streamlit as st
import pandas as pd
from git.repo.fun import touch

# title
st.title("Laptop Price Predictor")
# open files
pipe=pickle.load(open("pipe.pkl",'rb'))
df=pickle.load(open('df.pkl','rb'))


## brand
comapany=st.selectbox('Brand',df['Company'].unique())

## type name
type=st.selectbox('Type',df['TypeName'].unique())
# ram
ram=st.selectbox("RAM(in GB)",[2,4,6,8,12,16,24,32,64])
# weight
weight=st.number_input('Weight of the laptop')

# touchscreen
touchscreen=st.selectbox('Touchscreen',['Yes','No'])

# IPS
ips=st.selectbox('IPS',['Yes','No'])

#screen size
screen_size=st.selectbox("screen size in inches", [10.0,18.0,13.0])
## resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
# cpu
cpu=st.selectbox('CPU',df['Cpu brand'].unique())
# HDD
hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu=st.selectbox("GPU ",df['Gpu brand'].unique())
os=st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    # query
    ppi=None
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='Yes':
        ips=1

    else:
        ips=0

    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])
    ppi=((x_res**2)+(y_res**2))**0.5/screen_size
    query = pd.DataFrame([[comapany, type, ram, weight,screen_size, touchscreen, ips, ppi,
                           cpu, hdd, ssd, gpu, os]],
                         columns=['Company', 'TypeName', 'Ram', 'Weight','Inches', 'Touchscreen', 'IPS', 'ppi',
                                  'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'])

    #st.write("Query columns:", query.columns)

    #query=np.array([comapany,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
   # query=query.reshape(1,12) # Note the square brackets to create a single-row DataFrame

    st.title("The Predicted Price of this configuration is "+ str(int(np.exp(pipe.predict(query)[0]))))