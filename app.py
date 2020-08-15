import numpy as np
import pandas as pd
import pickle
import streamlit as st
import json

pickle_in =  open('BMI_calc.pkl','rb')
classifier = pickle.load(pickle_in)

def predict_note_authentication(Gender,Height,Weight):
    prediction = classifier.predict([[Gender,Height,Weight]])
    print(prediction)
    return prediction        

def main():
    #st.title("BMI CALCULATION")
    st.markdown("""<div style=text-align:center;"><h2><b>BMI CALCULATION</b></h2></div><br>""",unsafe_allow_html=True)
    html_temp = """
    <div style="background-color:tomato;padding:5px">
    <h3 style="color:#581845;text-align:center;"><b>Streamlit BMI calculator ML App </b></h3>
    </div><br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Gender = st.radio("Gender", ("Female","Male"))
    Height = st.number_input("Height in cm", min_value=140, max_value=199)
    Weight = st.number_input("Weight in kg", min_value=50, max_value=160)
    
    if Gender == "Female":
        Gender=0
    else:
        Gender=1
    
    #Storing Json file as object
    #Json_codes =  "C:/Users/Mari/Heroku/json_file.json"
    #Converting Gender values into number
    #Gender = Json_codes['Gender'][val]
    
    
    result = ""
    if st.button("Predict"):
        result= predict_note_authentication(Gender,Height,Weight)
    if result==0:
        st.success("Oops! Your are very Weak. Please increase your weight")
    if result==1:
        st.success("Oops! Your are Weak. Please increase your weight")
    if result==2:
        st.balloons()
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