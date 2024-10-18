import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
diabetes_model = pickle.load(open('diabete_model.sav', 'rb'))

# Background styling
page_bg_img = '''
<style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://github.com/SHAIK-RAIYAN-2022-CSE/malaria/blob/main/Images-free-abstract-minimalist-wallpaper-HD.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0); 
    }
    .block-container {
        max-width: 700px;
        margin: 50px auto;
        padding: 25px;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(12px);
        box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.8);
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
        background-color: #FF6347;
        color: white;
        font-size: 18px;
        padding: 12px 28px;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: white;
        color: #FF6347;
        border: 2px solid #FF6347;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white !important;
        text-align: center;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title
st.markdown("<h1>🔍 Diabetes Prediction using Machine Learning</h1>", unsafe_allow_html=True)

# Collect user input
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=0)
    BloodPressure = st.number_input('Blood Pressure value', min_value=0)
    Insulin = st.number_input('Insulin Level', min_value=0)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', min_value=0.0, step=0.01)

with col2:
    Glucose = st.number_input('Glucose Level', min_value=0)
    SkinThickness = st.number_input('Skin Thickness value', min_value=0)
    BMI = st.number_input('BMI value', min_value=0.0, step=0.1)
    Age = st.number_input('Age of the Person', min_value=1)

# Prediction logic
if st.button('Get Diabetes Test Result 🧪'):
    diab_prediction = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    )
    if diab_prediction[0] == 1:
        st.error('🚨 The person is diabetic.')
    else:
        st.success('✅ The person is not diabetic.')
