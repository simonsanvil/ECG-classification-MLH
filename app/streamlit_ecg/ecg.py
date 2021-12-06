import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np
import scipy.io
import pathlib
from tensorflow import keras


#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(page_title='ECG classification',
    layout='wide')

#---------------------------------#
# Data preprocessing and Model building

def read_ecg_preprocessing(uploaded_ecg):

      FS = 300
      maxlen = 30*FS

      uploaded_ecg.seek(0)
      mat = scipy.io.loadmat(uploaded_ecg)
      mat = mat["val"][0]

      uploaded_ecg = np.array([mat])

      X = np.zeros((1,maxlen))
      uploaded_ecg = np.nan_to_num(uploaded_ecg) # removing NaNs and Infs
      uploaded_ecg = uploaded_ecg[0,0:maxlen]
      uploaded_ecg = uploaded_ecg - np.mean(uploaded_ecg)
      uploaded_ecg = uploaded_ecg/np.std(uploaded_ecg)
      X[0,:len(uploaded_ecg)] = uploaded_ecg.T # padding sequence
      uploaded_ecg = X
      uploaded_ecg = np.expand_dims(uploaded_ecg, axis=2)
      return uploaded_ecg

def build_model(data):


    st.subheader('2. Model Prediction')

    model = load_model('ecg_streamlit/ResNet_30s_34lay_16conv.hdf5')

    classes = ['Atrial Fibrillation', 'Normal', 'Other Rhythm','Noise']

    prob = model.predict(data)
    ann = np.argmax(prob)
    #true_target =
    #print(true_target,ann)

    #confusion_matrix[true_target][ann] += 1
    return classes[ann],100*prob[0,ann]


#---------------------------------#
st.write("""
# ECG classification project

In this project, we used a pre trained model from the Physionet Cardiology challenge to detect heart anomalies like AF or arrythmia.


Try uploading your ECG!

""")

#---------------------------------#
# Sidebar - Collects user input features into dataframe
with st.sidebar.header('1. Upload your ECG'):
    uploaded_file = st.sidebar.file_uploader("Upload your ECG in mat. format", type=["mat"])

#---------------------------------#
# Main panel

if uploaded_file is not None:
    #st.write(uploaded_file)

    st.subheader('1.Visualize ECG')

    ecg = read_ecg_preprocessing(uploaded_file)

    st.line_chart(pd.DataFrame(np.concatenate(ecg).ravel().tolist()))

    #st.write(ecg)
    pred,conf = build_model(ecg)
    st.write("ECG classified as {}".format(pred))
    st.write("Confidence of the prediction: {:3.1f}%".format(conf))
