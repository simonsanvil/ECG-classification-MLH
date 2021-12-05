FROM python:3.8-buster

# Make sure pip and git are installed
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y git

# Upgrade pip
RUN pip3 install --upgrade pip

# clone the project repo
RUN git clone  https://github.com/simonsanvil/ECG-classification-MLH

# change to the app directory
WORKDIR /ECG-classification-MLH/app

# install the requirements
RUN pip3 install -r requirements.txt

# run the streamlit app
CMD ["streamlit", "run", "ecg_streamlit/ecg.py"]
