import pandas as pd
import os

def load_data(input_path):
    demographics = pd.read_csv(os.path.join(input_path, 'demographics.zip'))
    epidemiology = pd.read_csv(os.path.join(input_path, 'epidemiology.zip'))
    vaccinations = pd.read_csv(os.path.join(input_path, 'vaccinations.zip'))
    hospitalizations = pd.read_csv(os.path.join(input_path, 'hospitalizations.zip'))
    health = pd.read_csv(os.path.join(input_path, 'health.zip'))
    index = pd.read_csv(os.path.join(input_path, 'index.zip'))
    return demographics, epidemiology, vaccinations, hospitalizations, health, index