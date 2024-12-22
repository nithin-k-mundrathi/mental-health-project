import numpy as np
import pandas as pd
import pickle
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
        type: string
        required: true
      - depression_c: variance
        in: query
        type: string
        required: true
      - medical_c: variance
        in: query
        type: string
        required: true
      - alcohol_c: variance
        in: query
        type: string
        required: true
      - sleep_c: variance
        in: query
        type: string
        required: true
      - dietary_c: variance
        in: query
        type: string
        required: true
      - physical_c: variance
        in: query
        type: string
        required: true
      - smoker_c: variance
          in: query
          type: string
          required: true
      - marital_c: variance
          in: query
          type: string
          required: true
      - education_c: variance
          in: query
          type: string
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
    f1 = st.text_input("Number of Children","Should be less than 5")
    f2 = st.text_input("income_clipped","Type Here")
    f_subtance = st.text_input("substance_c","yes or no")
    f3 = 1 if f_subtance == 'Yes' else 0
    f_depression = st.text_input("depression_c","yes or no")
    f4 = 1 if f_depression == 'Yes' else 0
    f_medical = st.text_input("medical_c","yes or no")
    f5 = 1 if f_medical == 'Yes' else 0
    f_alcohol = st.text_input("alcohol_c","High or Medium or Low")
    f6 = 2 if f_alcohol == 'High' else (0 if f_alcohol == 'Low' else 1)
    f_sleep = st.text_input("sleep_c","Por or Fair or Good")
    f7 = 2 if f_sleep == 'Poor' else (0 if f_sleep == 'Fair' else 1)
    f_diet = st.text_input("dietary_c","Unhealthy or Healthy or Moderate")
    f8 = 2 if f_diet == 'Unhealthy' else (0 if f_diet == 'Healthy' else 1)
    f_physical = st.text_input("physical_c","Active or Moderate or Sedentary")
    f9 = 2 if f_physical == 'Sedentary' else (0 if f_physical == 'Active' else 1)
    f_smoker = st.text_input("smoker_c","Non-smoker or Former or Current")
    f10 = 2 if f_smoker == 'Current' else (0 if f_smoker == 'Non-smoker' else 1)
    f_marital = st.text_input("marital_c","Divorced or Widowed or Married or Single")
    f11 =  2 if (f_marital == 'Divorced') or (f_marital == 'Widowed')  else (0 if f_marital == 'Married' else 1)
    f_education = st.text_input("education_c","High School or Bachelor's Degree or Associate Degree or Master's Degree")
    f12 = 4 if (f_education == 'High School') else (3 if f_education == "Bachelor's Degree" else (2 if f_education == 'Associate Degree' else (0 if f_education == "Master's Degree" else 1)))
    f13 = st.text_input("age_c","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    