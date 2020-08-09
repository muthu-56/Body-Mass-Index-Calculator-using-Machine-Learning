import numpy as np
import pandas as pd
import pickle
import streamlit as st

pickle_in =  open('BMI_calc.pkl','rb')
classifier = pickle.load(pickle_in)

def predict_note_authentication(Gender,Height,Weight):
    prediction = classifier.predict([[Gender,Height,Weight]])
    return prediction        

def main():
    st.title("BMI CALCULATION")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit BMI calculator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.text_input("Gender", "Type Here... [Ex: For Male enter 1, Female enter 0]")
    Height = st.text_input("Height in cm", "Type Here")
    Weight = st.text_input("Weight in kg", "Type Here")
    result = ""
    if st.button("Predict"):
        result= predict_note_authentication(Gender,Height,Weight)
    if result==0:
        st.success("Oops! Your are very Weak. Please increase your weight")
    if result==1:
        st.success("Oops! Your are Weak. Please increase your weight")
    if result==2:
        st.success("Congrats! you are having good health condition.") 
    if result==3:
        st.success("Oops! Your are overweight. Please take care of your health")  
    if result==4:
        st.success("Oops! Your are Weak. Please increase your weight")  
    if result==5:
        st.success("Oops! Your are having Obesity. Please reduce your weight")
    if result==6:
        st.success("Oops! Your number say you are extremely Obese, keep an close eye on your health")    
    #st.success("The output is {}".format(result))
    
    
if __name__=='__main__':
    main()
