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
import rarfile
import gdown


def gbm_model():



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

    uploaded_file = st.file_uploader("Choose an MRI scan image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Fixed target size without any user input (default size)
        target_size = (284, 292)  # Default size

        # Preprocess the uploaded image
        img = Image.open(uploaded_file).resize(target_size)  # Resize to the default size
        img = img.convert('RGB')
        img_array = np.array(img) / 255.0  # Normalize the image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Display the uploaded image
        st.image(img, caption="Uploaded MRI Scan", use_container_width=True)

        # Prediction Logic
        if st.button("Analyze Scan"):
            with st.spinner("Analyzing..."):
                # Perform the prediction using the preprocessed image
                prediction = model.predict(img_array)  # Model prediction logic

                # Determine the result based on the model's prediction
                result = "No Glioblastoma" if prediction[0][0] > 0.5 else "Glioblastoma Detected"
            
                # Display the prediction result
                st.success(f"Prediction: {result}")

                # Generate PDF Report of the Model Result
                def generate_pdf(result, image_name):
                    # Create a temporary directory to store the image
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