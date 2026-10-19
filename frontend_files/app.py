import streamlit as st
import requests

st.title("SuperKart Sales Forecast")

product_id = st.text_input("Product ID")
store_id = st.text_input("Store ID")
mrp = st.number_input("Product MRP")

if st.button("Predict Sales"):
    payload = {"Product_Id": product_id, "Store_Id": store_id, "Product_MRP": mrp}
    # Replace with your Flask backend URL
    response = requests.post("http://localhost:5000/predict", json=payload)
    st.write("Predicted Sales:", response.json()["predicted_sales"])
