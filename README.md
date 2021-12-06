ECG-Classification
==============================

Web app to diagnose types of Arrhythmia from user-uploaded ECG signals using Machine Learning and Deeep Learning models.

[Try it yourself](https://ecg-classification.azurewebsites.net/)

Authors:
--------

- Andres Ruiz Calvo
- Daniel De Las Cuevas Turel
- Enrique Botía Barbera
- Simon E. Sanchez Viloria
- Zijun He


Requirements
----------
- python>=3.6

Usage
----------

### Run from the command line

```bash
# Create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# move to the directory app
cd app
# start the streamlit app
streamlit run streamlit_ecg/ecg.py
```

After running the commands above you'll be able to access the app from your local browser.

### Run with Docker

Use Docker to start the streamlit server to demo the app.

```bash
docker build -t ecg-classification-mlh .
# Wait until the image is built...
docker run ecg-classification-mlh
```


Reproducibility
----------

```python
#TODO
```

---------

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details. 
    |                         You can also store here documentation made with any other package.
    │                         e.g: pdoc --html ../src, make html, ...
    |
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── app                <- Directory where the web app is runned.
    │   ├── requirements.txt   <- specific dependencies of the streamlit app
    │   |
    │   ├── prod-config.toml <- configuration file for production
    │   |
    |   └───streamlit_ecg  <- Files used by the streamlit app.
    │       ├── ecg.py     <- The streamlit app itself.
    │       ├── validation/ <- sample ECGs for demonstration.
    │       └── model.mod <- The model used by the app to make predictions.        
    |
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    |
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
           └── visualize.py
    
    


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
