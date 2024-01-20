import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open('model(1).pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Customer Churn Prediction')

Customer_Age = st.number_input('Customer Age', min_value=18, max_value=100, step=1)
Dependent_count = st.number_input('Dependent Count', min_value=0, max_value=10, step=1)
Months_on_book = st.number_input('Months on Book', min_value=0, max_value=100, step=1)
Total_Relationship_Count = st.number_input('Total Relationship Count', min_value=0, max_value=10, step=1)
Months_Inactive_12_mon = st.number_input('Months Inactive 12 Mon', min_value=0, max_value=12, step=1)
Contacts_Count_12_mon = st.number_input('Contacts Count 12 Mon', min_value=0, max_value=10, step=1)
Credit_Limit = st.number_input('Credit Limit', min_value=0.0, step=0.1)
Total_Revolving_Bal = st.number_input('Total Revolving Bal', min_value=0, step=1)
Avg_Open_To_Buy = st.number_input('Avg Open To Buy', min_value=0.0, step=0.1)
Total_Amt_Chng_Q4_Q1 = st.number_input('Total Amt Chng Q4 Q1', min_value=0.0, step=0.01)
Total_Trans_Amt = st.number_input('Total Trans Amt', min_value=0, step=1)
Total_Trans_Ct = st.number_input('Total Trans Ct', min_value=0, step=1)
Total_Ct_Chng_Q4_Q1 = st.number_input('Total Ct Chng Q4 Q1', min_value=0.0, step=0.01)
Avg_Utilization_Ratio = st.number_input('Avg Utilization Ratio', min_value=0.0, step=0.01)

Marital_Status = st.selectbox('Marital Status', options=['Married', 'Single', 'Divorced', 'Unknown'])
Card_Category = st.selectbox('Card Category', options=['Blue', 'Silver', 'Gold', 'Platinum'])
Gender = st.selectbox('Gender', options=['M', 'F'])
Education_Level = st.selectbox('Education Level', options=['High School', 'Graduate', 'Uneducated', 'Post-Graduate', 'Doctorate', 'College'])

encoded_features = pd.get_dummies([Marital_Status, Card_Category, Gender, Education_Level],drop_first=True)
encoded_features = encoded_features.values.flatten()

Income_Category = st.selectbox('Income Category', options=["Less than $40K", "$40K - $60K", "$60K - $80K", "$80K - $120K", "$120K +"])
income_category_mapping = {"Less than $40K": 0, "$40K - $60K": 1, "$60K - $80K": 2, "$80K - $120K": 3, "$120K +": 4}
Income_Category_encoded = income_category_mapping[Income_Category]

model_input = [Customer_Age, Dependent_count, Income_Category_encoded, Months_on_book, Total_Relationship_Count, Months_Inactive_12_mon, Contacts_Count_12_mon, Credit_Limit, Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio] + list(encoded_features)

if st.button('Predict'):
    prediction = model.predict([model_input])[0]

    if prediction == 1:
        st.write('Prediction: The account is likely to be closed.')
    else:
        st.write('Prediction: The account is likely to remain active.')
