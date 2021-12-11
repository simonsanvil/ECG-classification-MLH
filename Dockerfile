FROM python:3.8-buster

# Make sure pip and git are installed
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y git

# Upgrade pip
RUN pip3 install --upgrade pip

# Add the project folder to the container
ADD app /app

# Add the models folder to the container
ADD models /models

# cd to the project folder
WORKDIR /app

# copy production config to .streamlit folder
RUN mkdir -p .streamlit/ && cp prod-config.toml .streamlit/config.toml

# install the requirements
RUN pip3 install -r requirements.txt

# run the streamlit app
CMD ["streamlit", "run", "streamlit_ecg/ecg.py"]