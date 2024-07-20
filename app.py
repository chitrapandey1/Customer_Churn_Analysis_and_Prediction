#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import json
import pickle
from sklearn.ensemble import RandomForestClassifier


# In[3]:


st.title('Customer Churn Prediction')

# Collect input data from user
customer_id = st.text_input('Customer ID')
monthlycharges = st.text_input('Monthly Charges')
totalcharges = st.text_input('Total Charges')
tenure = st.text_input('Tenure (in months)')
SeniorCitizen =  st.selectbox('Is customer the senior citizen?', options=['Yes', 'No'])
gender = st.selectbox('Gender', options=['Male', 'Female'])
partner = st.selectbox('Is customer married?', options=['Yes', 'No'])
dependents = st.selectbox('Does customer have dependants in his family?', options=['Yes', 'No'])
phservice = st.selectbox('Has customer subscribed for any additional phone service?', options=['Yes', 'No'])
intservice = st.selectbox('Does the customer avail internet services?', options=[ 'No', 'Fiber optic', 'DSL'])

if phservice == 'No':
    multilines = st.selectbox('Is the customer currently using multiple lines?', options=['No phone service'], index=0)
    olsecurity = st.selectbox('Does the customer have an active online security plan?', options=['No phone service'], index=0)
    olBackup = st.selectbox('Does the customer have any active additional backup service?', options=['No phone service'], index=0)
    devProc = st.selectbox('Does the customer have active device protection plan?', options=['No phone service'], index=0)
    techsupp = st.selectbox('Does the customer have have access to tech support?', options=['No phone service'], index=0)
    streamTV = st.selectbox('Does the customer use internet to stream TV?', options=['No phone service'], index=0)
    streamMovies = st.selectbox('Does the customer use internet to stream movies?', options=['No phone service'], index=0)
else:
    multilines = st.selectbox('Is the customer currently using multiple lines?', options=['Yes', 'No'])
    olsecurity = st.selectbox('Does the customer have an active online security plan?', options=['Yes', 'No'])
    olBackup = st.selectbox('Does the customer have any active additional backup service?', options=['Yes', 'No'])
    devProc = st.selectbox('Does the customer have have active device protection plan?', options=['Yes', 'No'])
    techsupp = st.selectbox('Does the customer have have access to tech support?', options=['Yes', 'No'])
    streamTV = st.selectbox('Does the customer use internet to stream TV?', options=['Yes', 'No'])
    streamMovies = st.selectbox('Does the customer use internet to stream movies?', options=['Yes', 'No'])

contract = st.selectbox('Current Contract Type', options=['Month-to-month', 'One year', 'Two year'])
billing = st.selectbox('Billing Type', options=['Paperless', 'Not Paperless'])
payment = st.selectbox('Payment Method', options=['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check'])


# In[ ]:


# Creating the dataframe
df = pd.DataFrame(columns=[
    'SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender_Female', 'gender_Male', 'Partner_No', 'Partner_Yes', 
    'Dependents_No', 'Dependents_Yes', 'PhoneService_No', 'PhoneService_Yes', 'MultipleLines_No', 'MultipleLines_No phone service', 
    'MultipleLines_Yes', 'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No', 'OnlineSecurity_No', 
    'OnlineSecurity_No internet service', 'OnlineSecurity_Yes', 'OnlineBackup_No', 'OnlineBackup_No internet service', 
    'OnlineBackup_Yes', 'DeviceProtection_No', 'DeviceProtection_No internet service', 'DeviceProtection_Yes', 'TechSupport_No', 
    'TechSupport_No internet service', 'TechSupport_Yes', 'StreamingTV_No', 'StreamingTV_No internet service', 'StreamingTV_Yes', 
    'StreamingMovies_No', 'StreamingMovies_No internet service', 'StreamingMovies_Yes', 'Contract_Month-to-month', 
    'Contract_One year', 'Contract_Two year', 'PaperlessBilling_No', 'PaperlessBilling_Yes', 'PaymentMethod_Bank transfer (automatic)', 
    'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check', 'tenure_group_1 - 12', 
    'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72'
])

# Populate the dataframe with the inputs
df.at[0, 'MonthlyCharges'] = int(monthlycharges)
df.at[0, 'TotalCharges'] = int(totalcharges)

# Senior Citizen
df.at[0, 'SeniorCitizen'] = 1 if SeniorCitizen == 'Yes' else 0

# Gender
df.at[0, 'gender_Female'] = 1 if gender == 'Female' else 0
df.at[0, 'gender_Male'] = 1 if gender == 'Male' else 0

# Partner
df.at[0, 'Partner_No'] = 1 if partner == 'No' else 0
df.at[0, 'Partner_Yes'] = 1 if partner == 'Yes' else 0

# Dependents
df.at[0, 'Dependents_No'] = 1 if dependents == 'No' else 0
df.at[0, 'Dependents_Yes'] = 1 if dependents == 'Yes' else 0

# Phone Service
df.at[0, 'PhoneService_No'] = 1 if phservice == 'No' else 0
df.at[0, 'PhoneService_Yes'] = 1 if phservice == 'Yes' else 0

# Multiple Lines
df.at[0, 'MultipleLines_No'] = 1 if multilines == 'No' else 0
df.at[0, 'MultipleLines_No phone service'] = 1 if multilines == 'No phone service' else 0
df.at[0, 'MultipleLines_Yes'] = 1 if multilines == 'Yes' else 0

# Internet Service
df.at[0, 'InternetService_DSL'] = 1 if intservice == 'DSL' else 0
df.at[0, 'InternetService_Fiber optic'] = 1 if intservice == 'Fiber optic' else 0
df.at[0, 'InternetService_No'] = 1 if intservice == 'No' else 0

# Online Security
df.at[0, 'OnlineSecurity_No'] = 1 if olsecurity == 'No' else 0
df.at[0, 'OnlineSecurity_No internet service'] = 1 if olsecurity == 'No internet service' else 0
df.at[0, 'OnlineSecurity_Yes'] = 1 if olsecurity == 'Yes' else 0

# Online Backup
df.at[0, 'OnlineBackup_No'] = 1 if olBackup == 'No' else 0
df.at[0, 'OnlineBackup_No internet service'] = 1 if olBackup == 'No internet service' else 0
df.at[0, 'OnlineBackup_Yes'] = 1 if olBackup == 'Yes' else 0

# Device Protection
df.at[0, 'DeviceProtection_No'] = 1 if devProc == 'No' else 0
df.at[0, 'DeviceProtection_No internet service'] = 1 if devProc == 'No internet service' else 0
df.at[0, 'DeviceProtection_Yes'] = 1 if devProc == 'Yes' else 0

# Tech Support
df.at[0, 'TechSupport_No'] = 1 if techsupp == 'No' else 0
df.at[0, 'TechSupport_No internet service'] = 1 if techsupp == 'No internet service' else 0
df.at[0, 'TechSupport_Yes'] = 1 if techsupp == 'Yes' else 0

# Streaming TV
df.at[0, 'StreamingTV_No'] = 1 if streamTV == 'No' else 0
df.at[0, 'StreamingTV_No internet service'] = 1 if streamTV == 'No internet service' else 0
df.at[0, 'StreamingTV_Yes'] = 1 if streamTV == 'Yes' else 0

# Streaming Movies
df.at[0, 'StreamingMovies_No'] = 1 if streamMovies == 'No' else 0
df.at[0, 'StreamingMovies_No internet service'] = 1 if streamMovies == 'No internet service' else 0
df.at[0, 'StreamingMovies_Yes'] = 1 if streamMovies == 'Yes' else 0

# Contract
df.at[0, 'Contract_Month-to-month'] = 1 if contract == 'Month-to-month' else 0
df.at[0, 'Contract_One year'] = 1 if contract == 'One year' else 0
df.at[0, 'Contract_Two year'] = 1 if contract == 'Two year' else 0

# Paperless Billing
df.at[0, 'PaperlessBilling_No'] = 1 if billing == 'Not Paperless' else 0
df.at[0, 'PaperlessBilling_Yes'] = 1 if billing == 'Paperless' else 0

# Payment Method
df.at[0, 'PaymentMethod_Bank transfer (automatic)'] = 1 if payment == 'Bank transfer (automatic)' else 0
df.at[0, 'PaymentMethod_Credit card (automatic)'] = 1 if payment == 'Credit card (automatic)' else 0
df.at[0, 'PaymentMethod_Electronic check'] = 1 if payment == 'Electronic check' else 0
df.at[0, 'PaymentMethod_Mailed check'] = 1 if payment == 'Mailed check' else 0

# Tenure
tenure = int(tenure)
if tenure <= 12:
    df[['tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']] = [1,0,0,0,0,0]
elif tenure <= 24:
    df[['tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']] = [0,1,0,0,0,0]
elif tenure <= 36:
    df[['tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']] = [0,0,1,0,0,0]
elif tenure <= 48:
    df[['tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']] = [0,0,0,1,0,0]
elif tenure <= 60:
    df[['tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']] = [0,0,0,0,1,0]
else:
    df[['tenure_group_1 - 12', 'tenure_group_13 - 24', 'tenure_group_25 - 36', 'tenure_group_37 - 48', 'tenure_group_49 - 60', 'tenure_group_61 - 72']] = [0,0,0,0,0,1]


# In[ ]:


# Load your model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


# if st.button('Predict'):
    # Make predictions
    prediction = model.predict(df)
    
    if prediction[0]==0:
        churn ='Will not churn'
        color = 'green'

    else:
         churn ='Will churn'
         color = 'red'


    # Display the prediction
    # st.write(f'Churn Prediction for Customer ID {customer_id}: {prediction[0]}')
    # st.text(f'Churn Prediction for Customer ID {customer_id}: {churn}')

    # Display the prediction in a colored text box with bold text
    st.markdown(
        f"""
        <div style="background-color:{color}; padding: 10px; border-radius: 5px; color: white;">
            <strong>Churn Prediction for Customer ID {customer_id}: {churn}</strong>
        </div>
        """,
        unsafe_allow_html=True
    )




