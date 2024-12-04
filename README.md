# Glioblastoma-Detection-Model

The main objectives of this project are:

To develop a CNN-based model that can accurately classify MRI scans of the brain.
To provide an easy-to-use interface where users can upload MRI images and receive predictions regarding the presence of Glioblastoma.
To provide a downloadable PDF report with the analysis results, which includes the prediction and the MRI scan image.
Data and Model
The model is trained using a dataset of MRI brain scans. The scans are processed and resized to fit the model input requirements, and then used to train the CNN to distinguish between Tumor (Glioblastoma) and Healthy scans. The model is evaluated on its ability to generalize to unseen data, ensuring high accuracy and reliability for clinical use.

Model Architecture
The model architecture used is a Convolutional Neural Network (CNN), which is ideal for image classification tasks. The network is trained to detect key features in MRI scans that are associated with Glioblastoma. This architecture is known for its efficiency in processing and analyzing visual data, especially in medical imaging.

Training the Model
The model was trained using labeled MRI scan data, where each scan was either labeled as "Tumor" or "Healthy." The data was preprocessed by resizing the images to a consistent size, normalizing pixel values, and augmenting the images to increase the robustness of the model.

How to Use
Upload an MRI Scan: Users can upload an MRI scan image (in JPG, PNG, or JPEG format) for analysis.
Model Prediction: The uploaded image will be processed and analyzed by the trained model.
Result: The model will predict whether the scan contains Glioblastoma or is Healthy.
Download Report: A PDF report will be generated with the result, including the image and the prediction details.
