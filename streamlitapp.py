import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabete_model.sav', 'rb'))
# page title

page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); /* Transparent header */
    }
    .block-container {
        max-width: 800px;
        margin: 50px auto; /* Center the content */
        padding: 20px;
        border: 2px solid #ccc; /* Full border */
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
        backdrop-filter: blur(10px); /* Background blur effect */
        box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.6); /* Box shadow for depth */
    }
    input {
        background-color: white !important;
        color: black !important;
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #4CAF50;
        border: 2px solid #4CAF50;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1>Diabetes Prediction using ML</h1>", unsafe_allow_html=True)


# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
    
with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if (diab_prediction[0] == 1):
      diab_diagnosis = 'The person is diabetic'
    else:
      diab_diagnosis = 'The person is not diabetic'
    
st.success(diab_diagnosis)
