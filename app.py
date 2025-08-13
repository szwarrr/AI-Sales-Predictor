import streamlit as st
import pandas as pd
from main import load_and_merge_data
from models.sales_predictor import train_sales_model
import os

st.title("📈 AI Sales Forecasting App")

st.markdown("Upload your **Sales**, **Features**, and **Stores** datasets below:")

sales_file = st.file_uploader("Upload sales.csv", type="csv")
features_file = st.file_uploader("Upload features.csv", type="csv")
stores_file = st.file_uploader("Upload stores.csv", type="csv")

if sales_file and features_file and stores_file:
    df = load_and_merge_data(sales_file, features_file, stores_file)
    st.success("✅ Data loaded and merged!")
    st.write("### Sample Data", df.head())

    if st.button("Train Model"):
        with st.spinner("Training model..."):
            mse = train_sales_model(df)
        st.success(f"🎯 Model trained! MSE = {mse:.2f}")