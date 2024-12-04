import streamlit as st
from importlib import import_module
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import joblib
from PIL import Image
from reportlab.pdfgen import canvas
from io import BytesIO
import os
import tempfile
import rarfile
import gdown

# Set up page configuration
st.set_page_config(page_title="Glioblastoma Detection Model")

# Initialize session state for page tracking
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Page navigation logic
def navigate_to(page_name):
    st.session_state["current_page"] = page_name

st.markdown("""
    <style>
        .stButton>button {
            width: 120px;  /* Adjust button width */
            margin-right: 5px;  /* Adjust spacing between buttons */
            padding: 8px 16px;  /* Adjust padding inside the button */
        }
    </style>
""", unsafe_allow_html=True)

# Top navigation bar using columns
col1, col2, col3, col4 = st.columns([0.01, 0.01, 0.01, 0.01])

with col1:
    if st.button("Home"):
        navigate_to("Home")
with col2:
    if st.button("Model"):
        navigate_to("Model")
with col3:
    if st.button("MRI Information"):
        navigate_to("MRI Information")
with col4:
    if st.button("About"):
        navigate_to("About")

# Render the selected page
current_page = st.session_state["current_page"]

# Add space for better layout
st.markdown(" ") 
st.markdown(" ") 
st.markdown(" ")
st.markdown(" ")
st.markdown(" ") 
st.markdown(" ") 
st.markdown(" ")
st.markdown(" ")


# Banner image
banner_image_path = "streamlit_img/medecinsansfrontiers.png"
banner_image = Image.open(banner_image_path)
st.image(banner_image, use_container_width=True)


st.markdown(" ")
st.markdown(" ") 
st.markdown(" ")
st.markdown(" ")

# Page content based on selected page
if current_page == "Home":
    st.title("Welcome to Glioblastoma Detection Model")
    st.markdown("""
    #### About This App
    Glioblastoma is one of the most aggressive types of brain cancer. Early and accurate detection can significantly impact treatment outcomes.
    This app uses a **Convolutional Neural Network (CNN)** trained on MRI images to detect Glioblastoma.
    """)
    
    st.markdown("### Glioblastoma Facts")
    st.markdown("""
    - **Prevalence**: Glioblastoma affects approximately 3 out of 100,000 people annually.
    - **Survival Rates**: The 5-year survival rate is only 5%.
    """)

elif current_page == "Model":
    st.title("Glioblastoma Model")
    model_module = import_module("child.model")
    model_module.gbm_model()  # Calls the 'gbm_model()' function from the Model page module
    st.write("Here, you can upload MRI scans for classification.")
    
elif current_page == "About":
    st.title("About this model")
    about_module = import_module("child.about")
    about_module.about_page()  # Calls the 'about_page()' function from the About page module

elif current_page == "MRI Information":
    st.title("About MRI Scans and Safety Usage")
    mri_module = import_module("child.mri_information")
    mri_module.mri_information()  # Calls the 'mri_information()' function from the MRI Information page module
