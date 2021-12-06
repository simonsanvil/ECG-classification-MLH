import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np
import scipy.io
# import pathlib
# from tensorflow import keras


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

    model = load_model('streamlit_ecg/ResNet_30s_34lay_16conv.hdf5')

    classes = ['Atrial Fibrillation', 'Normal', 'Other Rhythm','Noise']

    prob = model.predict(data)
    ann = np.argmax(prob)
    #true_target =
    #print(true_target,ann)

    #confusion_matrix[true_target][ann] += 1
    return classes[ann],prob #100*prob[0,ann]


#---------------------------------#
st.write("""
# ECG Classification

In this app, a pre-trained model from the [Physionet 2017 Cardiology Challenge](https://physionet.org/content/challenge-2017/1.0.0/) is used to detect heart anomalies like AF or arrythmia.

**Possible Predictions:** Atrial Fibrillation, Normal, Other Rhythm, Noise

### Authors:

- Andres Ruiz Calvo
- Daniel De Las Cuevas Turel
- Enrique Botía Barbera
- Simon E. Sanchez Viloria
- Zijun He


**Try uploading your own ECG!**

-------
""".strip())

hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {	
            visibility: hidden;
        }
        footer:after {
            content:'Made for Machine Learning in Healthcare with Streamlit';
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
        }
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#---------------------------------#
# Sidebar - Collects user input features into dataframe
with st.sidebar.header('1. Upload your ECG'):
    uploaded_file = st.sidebar.file_uploader("Upload your ECG in .mat format", type=["mat"])

st.sidebar.markdown("")

if uploaded_file is None:
    with st.sidebar.header('2. Or use a file from the validation set'):
        pre_trained_ecg = st.sidebar.selectbox(
            'Select a file from the training set',
            ['None','A00001.mat','A00002.mat','A00003.mat','A00004.mat',
            'A00005.mat','A00006.mat','A00007.mat','A00008.mat','A00009.mat'
            ],
            index=1
        )
        if pre_trained_ecg != "None":
            f = open("streamlit_ecg/validation/"+pre_trained_ecg, 'rb')
            if not uploaded_file:
                uploaded_file = f
        st.sidebar.markdown("Source: Physionet 2017 Cardiology Challenge")
else:
    st.sidebar.text ("Remove the file to use the validation set.")

#---------------------------------#
# Main panel

if uploaded_file is not None:
    #st.write(uploaded_file)

    st.subheader('1.Visualize ECG')

    ecg = read_ecg_preprocessing(uploaded_file)

    st.line_chart(pd.DataFrame(np.concatenate(ecg).ravel().tolist()))
    
    #st.write(ecg)
    pred,conf = build_model(ecg)
    classes = ['Atrial Fibrillation', 'Normal', 'Other Rhythm','Noise']
    mkd_pred_table = """
    | Rhythm Type | Confidence |
    | --- | --- |
    """ + "\n".join([f"| {classes[i]} | {conf[0][i]*100:.2f}% |" for i in range(len(classes))])

    st.write("ECG classified as **{}**".format(pred))
    pred_confidence = conf[0,np.argmax(conf)]*100
    st.write("Confidence of the prediction: **{:3.1f}%**".format(pred_confidence))
    st.write(f"**Likelihoods:**")
    st.markdown(mkd_pred_table, unsafe_allow_html=True)
