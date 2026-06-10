import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
import pickle

model=tf.keras.models.load_model('model.h5')

## load label_encoder_gender_pkl

with open('label_encode_gender.pkl','rb') as file:
    label_encoder_gender=pickle.load(file)

## load label one_hot_encoder

with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

## load one_hot_encode
with open('one_hot_encode.pkl','rb') as file:
    one_hot_encode_geo=pickle.load(file)


## Streamlit app
st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input("Age", min_value=18, max_value=100, value=35)

tenure = st.number_input("Tenure", min_value=0, max_value=20, value=3)

balance = st.number_input("Balance", min_value=0.0, value=40000.0)

num_products = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=10,
    value=2
)

has_credit_card = st.selectbox(
    "Has Credit Card",
    [0, 1]
)

is_active_member = st.selectbox(
    "Is Active Member",
    [0, 1]
)

estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=30000.0
)

if st.button("Predict Churn"):

    # Create DataFrame
    input_df = pd.DataFrame([{
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_products,
        'HasCrCard': has_credit_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary
    }])

    # Encode Gender
    input_df['Gender'] = label_encoder_gender.transform(
        input_df['Gender']
    )

    # Encode Geography
    geo_encoded = one_hot_encode_geo.transform(
        input_df[['Geography']]
    )

    geo_encoded_df = pd.DataFrame(
        geo_encoded,
        columns=one_hot_encode_geo.get_feature_names_out(
            ['Geography']
        )
    )

    # Merge Encoded Columns
    input_df = pd.concat(
        [
            input_df.drop('Geography', axis=1).reset_index(drop=True),
            geo_encoded_df.reset_index(drop=True)
        ],
        axis=1
    )

    # Scale Input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)

    prediction_proba = prediction[0][0]

    st.subheader("Prediction Result")
    st.write(f"Churn Probability: {prediction_proba:.2%}")

    if prediction_proba > 0.5:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")