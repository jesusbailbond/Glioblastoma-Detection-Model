import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import joblib
from PIL import Image
from reportlab.pdfgen import canvas
from io import BytesIO
import os
import tempfile
from about import about_page
from mri_information import mri_information
import rarfile
import gdown


banner_image_path = "streamlit_img/medecinsansfrontiers.png"
banner_image = Image.open(banner_image_path)
st.image(banner_image, use_container_width=True)

st.markdown(" ")  # One blank line
st.markdown(" ") 
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")


# Sidebar panel selection logic
st.sidebar.header("Main Panel")
image_processing_button = st.sidebar.button("Image Processing Settings")

# Initialize session state for panel
if "panel" not in st.session_state:
    st.session_state.panel = "Image Processing Settings"

# Switch panel content based on button clicks

if image_processing_button:
    st.session_state.panel = "Image Processing Settings"



# Logic for Image Processing Settings Panel
if st.session_state.panel == "Image Processing Settings":
    st.sidebar.subheader("Image Processing Settings")
    resize_option = st.sidebar.radio("Choose Image Size", ["Default (284x292)", "Custom"], key="resize_option_radio")
    st.sidebar.markdown("""
    You can choose to resize the uploaded MRI scans to a default size or a custom size.
    The custom option allows you to manually input the width and height for resizing.
    """)
    
    if resize_option == "Default (284x292)":
        target_size = (284, 292)
    else:
        width = st.sidebar.number_input("Enter width", min_value=1, value=284)
        height = st.sidebar.number_input("Enter height", min_value=1, value=292)
        target_size = (width, height)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", ["Home", "Model", "About", "MRI Informations"])

# Content based on page selection
if page == "Home":
    st.title("Welcome to Glioblastoma Detection")
    
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
    
    # Sidebar content for Home page
    st.sidebar.subheader("Home Sidebar")
    st.sidebar.write("Navigate to other sections to explore more.")
        # Custom sidebar content for Home page
    st.sidebar.subheader("Home Sidebar")
    st.sidebar.write("This is the sidebar for the Home page.")

elif page == "Model":
    st.title("Model")
    st.write("Here, you can upload MRI scans for classification.")
    st.sidebar.subheader("Model Sidebar")
    st.sidebar.write("This is the sidebar for the Model page.")
    st.sidebar.button("Start Model Analysis")
# Main Page Content


# Check if model is already in session state, if not, load it
    if 'model' not in st.session_state:
        url = "https://drive.google.com/uc?id=14dzJPEd_RSJS3jfY9EwJGEfH0aRlu7zq"
        output = "model_export.pkl"
    
    # Download the model file
        gdown.download(url, output, quiet=False)
    
    # Load the model using joblib
        model = joblib.load('model_export.pkl')
    
    # Store the model in session state
        st.session_state.model = model
    else:
        model = st.session_state.model


    #Page title and text    
    st.title("Glioblastoma Detection")
    st.markdown("""
    This web app uses a trained **Convolutional Neural Network (CNN)** model to predict the presence of Glioblastoma from MRI scans. 
    Upload an MRI scan, and the model will analyze it and predict whether the scan is likely to show signs of Glioblastoma.
    """)
    st.write("Upload an MRI image to classify it.")

# Upload the image for the model
    uploaded_file = st.file_uploader("Choose an MRI scan image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
    # Preprocess the uploaded image
        img = Image.open(uploaded_file).resize(target_size)  # Resize based on the selected option in the sidebar
        img = img.convert('RGB')
        img_array = np.array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Display the uploaded image
        st.image(img, caption="Uploaded MRI Scan", use_container_width=True)

# Prediction Logic
    if uploaded_file is not None and st.button("Analyze Scan"):
        with st.spinner("Analyzing..."):
        # Perform the prediction using the preprocessed image
            prediction = model.predict(img_array)  # Model prediction logic

        # Determine the result based on the model's prediction
            result = "No Glioblastoma" if prediction[0][0] > 0.5 else "Glioblastoma Detected"
        
        # Display the prediction result
            st.success(f"Prediction: {result}")

    # Generate PDF Report of the Model Result
        def generate_pdf(result, image_name):
        # Create a ^porary directory to store the image
            temp_dir = tempfile.mkdtemp()

        # Save the uploaded image to a temporary file
            uploaded_img = Image.open(uploaded_file)  # Assuming uploaded_file is still in memory
            temp_img_path = os.path.join(temp_dir, image_name)

            uploaded_img.save(temp_img_path)

        # Create the PDF
            pdf_path = os.path.join(temp_dir, f"{image_name}_result.pdf")
            c = canvas.Canvas(pdf_path)

        # Add the result text and image to the PDF
            c.drawString(100, 800, f"Prediction: {result}")
            c.drawImage(temp_img_path, 100, 400, width=200, height=200)

        # Save the PDF
            c.save()

            return pdf_path

    # Generate the PDF with the result
        pdf_path = generate_pdf(result, uploaded_file.name)

    # Allow user to download the generated PDF
        with open(pdf_path, "rb") as f:
            st.download_button("Download PDF", f, file_name="scan_result.pdf")




elif page == "About":
    st.title("About this model")
    about_page()
    # Custom sidebar content for About page
    st.sidebar.subheader("About Sidebar")
    st.sidebar.write("This is the sidebar for the About page.")


elif page == "MRI Informations":
    st.title("About MRI Scans and Safety Usage")
    mri_information()
    st.sidebar.subheader("MRI Infos Sidebar")
    st.sidebar.write("This is the sidebar for the MRI Informations Page.")
