import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

model = pickle.load(open("model.pkl", "rb"))
st.title(":red[Flipkart Laptop Price Prediction]")

st.header("Laptop Price Predictor!!!")
#['Processor_type', 'RAM_GB', 'RAM_type', 'Disk_Type', 'Disk_size', 'OS','Display_inches']

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH_1 = os.path.join(FILE_DIR,"laptop_price.csv")
DATA_PATH_2 = os.path.join(FILE_DIR,"laptop_price_2.csv")

df=pd.read_csv(DATA_PATH_1)
data=df.copy()

df2=pd.read_csv(DATA_PATH_2)
data2=df2.copy()

dic={}
for colums in data.columns:
    print(colums)
    dic.update(dict(zip(data[colums].unique(),data2[colums].unique())))

print(dic)

val1 = st.selectbox(
    'Processor_type',
    (data["Processor_type"].unique()))

val2 = st.selectbox(
    'RAM_GB',
    (data["RAM_GB"].unique()))

val3 = st.selectbox(
    'RAM_type',
    (data["RAM_type"].unique()))

val4 = st.selectbox(
    'Disk_Type',
    (data["Disk_Type"].unique()))

val5 = st.selectbox(
    'Disk_size',
    (data["Disk_size"].unique()))

val6 = st.selectbox(
    'OS',
    (data["OS"].unique()))


val7 = st.selectbox(
    'Display_inches',
    (data["Display_inches"].unique()))


value=[dic[val1],dic[val2],dic[val3],dic[val4],dic[val5],dic[val6],dic[val7]]
print(value)
price = model.predict([value])
print(price)

st.write('\n\tPrice of the laptop approxmately ₹', abs(int(price)))