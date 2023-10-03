FROM python:3.8-buster

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

# Add streamlit folder to the container
ADD .streamlit /.streamlit

# rename production config file to config to use the production configuration in streamlit
RUN cp .streamlit/prod-config.toml .streamlit/config.toml

# install the requirements
RUN pip3 install -r app/requirements.txt

# run the streamlit app
CMD ["streamlit", "run", "app/main.py"]