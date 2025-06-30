import streamlit as st
import pandas as pd
import joblib

model= joblib.load("fraud_detection_model.pkl")
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and use the predict button")
st.divider()

transaction_type=st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASHOUT", "DEPOSIT"])
amount=st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalance_orig=st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalance_orig=st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalance_dest=st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalance_dest=st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalance_orig,
        "newbalanceOrig": newbalance_orig,
        "oldbalanceDest": oldbalance_dest,
        "newbalanceDest": newbalance_dest
    }, index=[0])
    
    prediction = model.predict(input_data)[0]
    
    st.subheader(f"Prediction :'{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction is likely to be fraudulent.")
    else:
        st.success("This transaction is likely to be legitimate.")