import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model


model=load_model("./maternal_ann.keras")

scaler=joblib.load("scaler.pkl")

encoder=joblib.load("label_encoder.pkl")


age=st.number_input("Age : ",16,60,25)

systolic=st.number_input("Systolic BP : ")

diastolic=st.number_input("Diastolic BP : ")

bs=st.number_input("Blood Sugar : ")

temparature=st.number_input("Temparature : ")

heartrate=st.number_input("Heart Rate : ")

if st.button("Predict risk"):
    sample=np.array([[
        age,systolic,diastolic,bs,temparature,heartrate
   ]])
    
    sample=scaler.transform(sample)

    prediction=model.predict(sample)

    index=np.argmax(prediction)

    result=encoder.inverse_transform([index])[0]

    confidence=prediction[0][index]*100

    st.success(f"Prediction : {result}")
    st.info(f"Confidence : {confidence} %")

    st.write("Class Probabilities")

    st.write(prediction)
    st.write(encoder.classes_)


# 19,120,80,7,98,70,mid risk

# 23,90,60,7.01,98,76,low risk

    


