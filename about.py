import streamlit as st

def about_page():
    # About page content in markdown format
    about_text = """
    # About the Glioblastoma Detection Project

    ## Overview

    Glioblastoma (GBM) is one of the most aggressive and deadly types of brain cancer. Early detection plays a crucial role in improving patient outcomes and guiding treatment decisions. In this project, we aim to develop a predictive model that can analyze MRI scans and detect the presence of Glioblastoma. 

    Using Convolutional Neural Networks (CNNs), we train a model on MRI scan images, which are typically used in medical imaging to detect abnormalities like tumors in the brain. The model's ability to accurately classify scans as either containing Glioblastoma or being healthy will support healthcare professionals in making faster and more accurate diagnoses.

    ## Objective

    The main objectives of this project are:

    - To develop a CNN-based model that can accurately classify MRI scans of the brain.
    - To provide an easy-to-use interface where users can upload MRI images and receive predictions regarding the presence of Glioblastoma.
    - To provide a downloadable PDF report with the analysis results, which includes the prediction and the MRI scan image.

    ## Data and Model

    The model is trained using a dataset of MRI brain scans. The scans are processed and resized to fit the model input requirements, and then used to train the CNN to distinguish between **Tumor** (Glioblastoma) and **Healthy** scans. The model is evaluated on its ability to generalize to unseen data, ensuring high accuracy and reliability for clinical use.

    ### Model Architecture

    The model architecture used is a Convolutional Neural Network (CNN), which is ideal for image classification tasks. The network is trained to detect key features in MRI scans that are associated with Glioblastoma. This architecture is known for its efficiency in processing and analyzing visual data, especially in medical imaging.

    ### Training the Model

    The model was trained using labeled MRI scan data, where each scan was either labeled as "Tumor" or "Healthy." The data was preprocessed by resizing the images to a consistent size, normalizing pixel values, and augmenting the images to increase the robustness of the model.

    ## How to Use

    1. **Upload an MRI Scan**: Users can upload an MRI scan image (in JPG, PNG, or JPEG format) for analysis.
    2. **Model Prediction**: The uploaded image will be processed and analyzed by the trained model.
    3. **Result**: The model will predict whether the scan contains **Glioblastoma** or is **Healthy**.
    4. **Download Report**: A PDF report will be generated with the result, including the image and the prediction details.

    ## Future Work

    While the current model focuses on detecting Glioblastoma, the goal is to expand it to identify other types of brain tumors and abnormalities. By incorporating more data, including scans from various imaging modalities (e.g., T1, T2, and T3 MRI sequences), the model’s accuracy and range can be improved.

    ## Challenges

    During the development of the model, some of the challenges faced included:
    - **Data Imbalance**: The dataset may have more healthy scans than tumor scans, leading to class imbalance. Techniques like class weighting or resampling can be used to address this.
    - **Generalization**: Ensuring that the model generalizes well to unseen scans is critical. Regular validation using a separate test set was essential to mitigate overfitting.

    ## Technologies Used

    - **Python**: The programming language for model development, data manipulation, and web application deployment.
    - **Streamlit**: Framework used for building interactive and user-friendly web applications for displaying predictions and results.
    - **TensorFlow/Keras**: Deep learning libraries used for developing, training, and deploying the Convolutional Neural Network (CNN) model to detect Glioblastoma.
    - **Joblib**: Library for saving and loading the trained machine learning models, ensuring efficient deployment and reusability.
    - **ReportLab**: A library used to generate dynamic PDF reports containing MRI scan images and their corresponding predictions.
    - **PIL (Pillow)**: Python Imaging Library, utilized for loading, manipulating, and preprocessing MRI scan images before passing them to the model.
    - **Matplotlib & Seaborn**: Used for data visualization and displaying model results, including the creation of charts and plots.
    - **Plotly**: Interactive plotting library used for building dynamic visualizations, especially helpful in exploring the model’s performance.
    - **nbia**: Part of the TCIA (The Cancer Imaging Archive) utilities, which allows you to access and download medical imaging data for training and evaluating the model.
    - **Scikit-learn**: Utilized for computing class weights, especially useful in handling class imbalance during model training.
    - **NumPy**: A fundamental package for scientific computing with Python, used for manipulating arrays and performing mathematical operations on image data.
    - **Shutil & Random**: Used for file manipulation and creating randomized data splits, respectively.

    ## Acknowledgments

    We would like to thank the open-source communities and datasets that made this project possible. The dataset used for training the model was sourced from the **The Cancer Imaging Archive (TCIA) API**, which provides access to a large collection of medical imaging data, including MRI scans. The tools used in the development were open-source, which helped reduce costs and time.
    """

    st.markdown(about_text)