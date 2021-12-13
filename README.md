ECG-Classification
==============================

[![Deploy to Azure Web App](https://github.com/simonsanvil/ECG-classification-MLH/actions/workflows/master_ecg-classification.yml/badge.svg)](https://github.com/simonsanvil/ECG-classification-MLH/actions/workflows/master_ecg-classification.yml)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/simonsanvil/ECG-classification-MLH/HEAD)[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simonsanvil/ECG-classification-MLH) 

[![!discord](https://img.shields.io/static/v1?logo=discord&label=discord&message=chat&color=lightgreen)](https://discord.gg/tfy6dDKgcP)

Web app to diagnose types of Arrhythmia from user-uploaded ECG signals using Machine Learning and Deeep Learning models.

The data used to train and test the models used by this app comes from the [PhysioNet 2017 AF Classification Challenge](https://physionet.org/content/challenge-2017/1.0.0/).

Try the app yourself [here](https://ecg-classification.azurewebsites.net/).

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
# start the streamlit app
streamlit run app/main.py
```

After running the commands above you'll be able to access the app from your local browser.

### Run with Docker

Use Docker to start the streamlit server to demo the app.

```bash
docker build -t ecg-classification .
# Wait until the image is built...
docker run ecg-classification
```

Reproducibility
----------

1. Clone this repository.
2. Go to the notebooks folder and explore our analysis or open the notebook used to train the model here [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/simonsanvil/ECG-classification-MLH/blob/master/notebooks/ECG-Zijun.ipynb)

3. Train the models yourself or load the pre-trained weights that we've provided in the models/ folder.
4. Run the streamlit app to see the results.

References
----------

> Goldberger, A., et al. "PhysioBank, PhysioToolkit, and PhysioNet:
Components of a new research resource for complex physiologic signals.
Circulation [Online]. 101 (23), pp. e215–e220." (2000).


-------

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
