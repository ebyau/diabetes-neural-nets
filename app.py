import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
import numpy as np




#loading the trained model
model = load_model('diabetes_model.h5')

@st.cache(allow_output_mutation=True)

def prediction(preg,gluc,bloodpress,skinthick,insulin,bmi,dpf,age):
       
    # making predictions
    predictions = model.predict(
        [[preg,gluc,bloodpress,skinthick,insulin,bmi,dpf,age]])
#     predictions = predictions.reshape(1, -1)
    
    if predictions == 0:
        pred = 'Diabetic Case'
    else:
        pred = 'Non-Diabetic'
    return pred
   
          
         
   
        
# main function defines our webpage

def main():
    
     # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Diabetic Hub</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    
        
    # allow user input 
    preg = st.number_input('Pregnancies',min_value=0, max_value=100, value=10, step=1)
    gluc = st.number_input('Glucose',min_value=0, max_value=1000, value=10, step=1)
    bloodpress  = st.number_input('Blood Pressure',min_value=0, max_value=400, value=0, step=1)
    skinthick = st.number_input('Skin Thickness',min_value=0, max_value=10000, value=0, step=1)
    insulin  = st.number_input('Insulin',min_value=0, max_value=1000, value=10, step=1)
    bmi  = st.number_input('BMI',min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
    dpf = st.number_input('Diabetes Pedigree Function',min_value=0.000, max_value=1000.000, value=0.000, step=0.001)
    age  = st.number_input('Age',min_value=1, max_value=100, value=10, step=1)
    
       
    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(preg,gluc,bloodpress,skinthick,insulin,bmi,dpf,age)
        
        st.success('{}'.format(result))
     #   st.success('probs {}' .format(preds))
        
if __name__=='__main__': 
    main()
