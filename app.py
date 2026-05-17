import tensorflow as tf
import streamlit as st
import numpy as np
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
import pandas as pd
import pickle

# Load the model and preprocessing objects
model=tf.keras.models.load_model("model.h5")

#load the encoder and scalers
with open("one_hot_encoder_geo.pkl","rb") as file:
    one_hot_encoder_geo=pickle.load(file)

with open("Label_encoder_gender.pkl","rb") as file:
    Label_encoder_gender=pickle.load(file)

with open("scaler.pkl","rb") as file:
    scaler=pickle.load(file)

#STREAMLIT APP
st.title("Customer Churn Prediction")

# Create input fields for user data
geography=st.selectbox("Geography",one_hot_encoder_geo.categories_[0])
gender=st.selectbox("Gender",Label_encoder_gender.classes_)
age=st.slider("AGE",18,100)
balance=st.number_input("Balance")
credit_score=st.slider("Credit Score")
tenure=st.slider("Tenure",0,10)
num_of_products=st.slider("Number of Products",1,4)
has_cr_card=st.selectbox("Has Credit Card",[0,1])
is_active_member=st.selectbox("Is Active Member",[0,1])
estimated_salary=st.number_input("Estimated Salary")

# Create a dictionary to hold the input data
input_data=pd.DataFrame({
    "CreditScore":[credit_score],
    "Gender": [Label_encoder_gender.transform([gender])[0]],
    "Age": [age],
    "Balance": [balance],
    "Tenure": [tenure],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "EstimatedSalary": [estimated_salary]  
})

#one hot encoding for geography
geo_encoder=one_hot_encoder_geo.transform([[geography]]).toarray()
one_hot_encoded_geo_df=pd.DataFrame(geo_encoder,columns=one_hot_encoder_geo.get_feature_names_out(["Geography"]))

# COMBINE THE INPUT DATA WITH ONE HOT ENCODED COLUMNS
input_data=pd.concat([input_data.reset_index(drop=True),one_hot_encoded_geo_df],axis=1)

# Scale the input data
input_data = input_data[scaler.feature_names_in_]
input_scaled = scaler.transform(input_data)

#predict the churn probability
prediction=model.predict(input_scaled)
prediction_probability=prediction[0][0]

# Display the prediction result

st.write(f"Churn Probability: {prediction_probability:.4f}")

if prediction_probability > 0.5:
    st.write("The customer is likely to churn.")
else:
    st.write("The customer is not likely to churn.")

