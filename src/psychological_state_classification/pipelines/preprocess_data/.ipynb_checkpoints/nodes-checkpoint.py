"""
This is a boilerplate pipeline 'preprocess_data'
generated using Kedro 0.19.10
"""
import pandas as pd

def parse_eeg_bands(x :pd.Series):
    """
    Parse the string representation of a list of EEG bands (Delta, ALPHA and Beta bands)
    into a list of floats.
    """
    x = x.replace('[','').replace(']','')
    x = x.split(',', expand=True).astype(float)
    return x

def parse_blood_pressure(x :pd.Series):
    """
    Parse the string representation of a blood pressure (Systolic/Diastolic) 
    into a list of floats.
    """
    x = x.str.split('/', expand=True)
    print(type(x))
    return x
