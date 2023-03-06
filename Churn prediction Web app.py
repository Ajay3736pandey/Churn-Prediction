# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:41:17 2023

@author: ajay3
"""

import numpy as np 
import pickle 
import streamlit as st 

 # Loading the saved model 
loaded_model = pickle.load(open("trained_model.sav",'rb'))


# creating the function for prediction 
def Churn_prediction (input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person has not churned'
    else:
      return 'The person has churned'
  
    
def main():
    
    # Title 
    st.title('Churn Prediction Web App')
    
    
    # Getting input from user 
    
    voice_plan = st.selectbox('Voiceplan',('1','0'))
    voice_messages = st.number_input('Insert no of voice_message')
    intl_plan = st.selectbox('Intlplan',('1','0'))
    intl_mins = st.number_input('Insert intl mins')
    intl_calls = st.number_input('Insert intl calls')
    intl_charge = st.number_input('Insert intl charge')
    day_mins = st.number_input('Insert day mins')
    day_calls = st.number_input('Insert day calls')
    day_charge = st.number_input('Insert day charge')
    eve_mins = st.number_input('Insert eve mins')
    eve_calls = st.number_input('Insert eve calls')
    eve_charge = st.number_input('Insert eve charge')
    night_mins = st.number_input('Insert night mins')
    night_calls = st.number_input('Insert night calls')
    night_charge = st.number_input('Insert night charge')
    customer_calls = st.number_input('Insert no of customer_calls')
    
    
    
    # Code For Prediction 
    Result = ''
    
    # Creating a Button For Prediction 
    if st.button('Churn Result'):
        Result = Churn_prediction([voice_plan,voice_messages,intl_plan,intl_mins,intl_calls,intl_charge,day_mins,day_calls,day_charge,eve_mins,eve_calls,eve_charge,night_mins,night_calls,night_charge,customer_calls])
        
        
    st.success(Result)
    
    
    
if __name__ == '__main__':
    main() 
