import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
import scipy.io
# import pathlib
# from tensorflow import keras
from src.visualization import plot_ecg

#---------------------------------#
# Page layout
## Page expands to full width
st.set_page_config(
    page_title='🫀 ECG Classification',
    # anatomical heart favicon
    page_icon="https://api.iconify.design/openmoji/anatomical-heart.svg?width=500",
    layout='wide'
)

# PAge Intro
st.write("""
# 🫀 ECG Classification

For this app, we trained a model to detect heart anomalies based on the [Physionet 2017 Cardiology Challenge](https://physionet.org/content/challenge-2017/1.0.0/) 
dataset.

**Possible Predictions:** Atrial Fibrillation, Normal, Other Rhythm, or Noise

### Authors:

- Simon E. Sanchez Viloria
- Andres Ruiz Calvo
- Daniel De Las Cuevas Turel
- Enrique Botía Barbera
- Zijun He


**Try uploading your own ECG!**

-------
""".strip())

#---------------------------------#
# Data preprocessing and Model building

@st.cache_data
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

model_path = 'models/weights-best.hdf5'
classes = ['Normal','Atrial Fibrillation','Other','Noise']

@st.cache_resource
def get_model(model_path):
    model = load_model(f'{model_path}')
    return model

@st.cache_resource
def get_prediction(data,_model):
    prob = _model(data)
    ann = np.argmax(prob)
    #true_target =
    #print(true_target,ann)

    #confusion_matrix[true_target][ann] += 1
    return classes[ann],prob #100*prob[0,ann]


# Visualization --------------------------------------
@st.cache_resource
def visualize_ecg(ecg,FS):
    fig = plot_ecg(uploaded_ecg=ecg, FS=FS)
    return fig


#Formatting ---------------------------------#

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

file_gts = {
    "A00001" : "Normal",
    "A00002" : "Normal",
    "A00003" : "Normal",
    "A00004" : "Atrial Fibrilation",
    "A00005" : "Other",
    "A00006" : "Normal",
    "A00007" : "Normal",
    "A00008" : "Other",
    "A00009" : "Atrial Fibrilation",
    "A00010" : "Normal",
    "A00015" : "Atrial Fibrilation",
    "A00205" : "Noise",
    "A00022" : "Noise",
    "A00034" : "Noise",
}
valfiles = [
    'None',
    'A00001.mat','A00010.mat','A00002.mat','A00003.mat',
    "A00022.mat", "A00034.mat",'A00009.mat',"A00015.mat",
    'A00008.mat','A00006.mat','A00007.mat','A00004.mat',
    "A00205.mat",'A00005.mat'
]

if uploaded_file is None:
    with st.sidebar.header('2. Or use a file from the validation set'):
        pre_trained_ecg = st.sidebar.selectbox(
            'Select a file from the validation set',
            valfiles,
            format_func=lambda x: f'{x} ({(file_gts.get(x.replace(".mat","")))})' if ".mat" in x else x,
            index=1,

        )
        if pre_trained_ecg != "None":
            f = open("data/validation/"+pre_trained_ecg, 'rb')
            if not uploaded_file:
                uploaded_file = f
        st.sidebar.markdown("Source: Physionet 2017 Cardiology Challenge")
else:
    st.sidebar.markdown("Remove the file above to demo using the validation set.")

st.sidebar.markdown("---------------")
st.sidebar.markdown("Check the [Github Repository](https://github.com/simonsanvil/ECG-classification-MLH) of this project")
#---------------------------------#
# Main panel

model = get_model(f'{model_path}')

if uploaded_file is not None:
    #st.write(uploaded_file)
    col1,_,col2 = st.columns((0.5,.05,0.45))

    with col1: # visualize ECG
        st.subheader('1.Visualize ECG')
        ecg = read_ecg_preprocessing(uploaded_file)
        
        fig = visualize_ecg(ecg, FS=300)
        st.pyplot(fig, use_container_width=True)
        

    with col2: # classify ECG
        st.subheader('2. Model Predictions')
        with st.spinner(text="Running Model..."):
            pred,conf = get_prediction(ecg,model)
        mkd_pred_table = [
            "| Rhythm Type | Confidence |",
            "| --- | --- |"
        ]
        for i in range(len(classes)):
            mkd_pred_table.append(f"| {classes[i]} | {conf[0,i]*100:3.1f}% |")
        mkd_pred_table = "\n".join(mkd_pred_table)

        st.write("ECG classified as **{}**".format(pred))
        pred_confidence = conf[0,np.argmax(conf)]*100
        st.write("Confidence of the prediction: **{:3.1f}%**".format(pred_confidence))
        st.write(f"**Likelihoods:**")
        st.markdown(mkd_pred_table)

    # st.line_chart(np.concatenate(ecg).ravel().tolist())
