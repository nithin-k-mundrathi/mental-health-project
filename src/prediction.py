import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("models/model.pkl","rb")
load_model=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13):
    
    """Let's find if a person has Mental Illnes 
    This is using docstrings for specifications.
    ---
    parameters:  
      - Number of Children: variance
        in: query
        type: number
        required: true
      - name: income_clipped
        in: query
        type: number
        required: true
      - substance_c: variance
        in: query
        type: number
        required: true
      - depression_c: variance
        in: query
        type: number
        required: true
      - medical_c: variance
        in: query
        type: number
        required: true
      - alcohol_c: variance
        in: query
        type: number
        required: true
      - sleep_c: variance
        in: query
        type: number
        required: true
      - dietary_c: variance
        in: query
        type: number
        required: true
      - physical_c: variance
        in: query
        type: number
        required: true
	  - smoker_c: variance
        in: query
        type: number
        required: true
	  - marital_c: variance
        in: query
        type: number
        required: true
	  - education_c: variance
        in: query
        type: number
        required: true
	  - age_c: variance
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=load_model.predict([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

def main():
    st.title("Mental health Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Mental Health Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    f1 = st.text_input("Number of Children","Type Here")
    f2 = st.text_input("income_clipped","Type Here")
    f3 = st.text_input("substance_c","Type Here")
    f4 = st.text_input("depression_c","Type Here")
    f5 = st.text_input("medical_c","Type Here")
    f6 = st.text_input("alcohol_c","Type Here")
    f7 = st.text_input("sleep_c","Type Here")
    f8 = st.text_input("dietary_c","Type Here")
    f9 = st.text_input("physical_c","Type Here")
    f10 = st.text_input("smoker_c","Type Here")
    f11 = st.text_input("marital_c","Type Here")
    f12 = st.text_input("education_c","Type Here")
    f13 = st.text_input("age_c","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    