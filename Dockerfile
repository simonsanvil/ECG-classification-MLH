FROM python:3.8-buster

# Make sure pip and git are installed
RUN apt-get update && apt-get install -y python3-pip && apt-get install -y git

# Upgrade pip
RUN pip3 install --upgrade pip

# Add the project folder to the container
ADD app /app

# Add src folder to the container
ADD src /src

# Add setup.py to the container in order to install the project's codebase
ADD setup.py setup.py

# Add the data folder to the container
ADD data /data

# Add the models folder to the container
ADD models /models

# copy production config to .streamlit folder
RUN mkdir -p .streamlit/ && cp app/prod-config.toml .streamlit/config.toml

# install the requirements
RUN pip3 install -r app/requirements.txt

# run the streamlit app
CMD ["streamlit", "run", "app/main.py"]