#!/usr/bin/env python3
"""Helper script to prepare the Kaggle diabetes dataset.

Usage:
    python download_kaggle_data.py

This script prints the exact folder path and the recommended Kaggle command.
It does not download the dataset automatically because Kaggle requires authentication.
"""

import os

DATA_DIR = "data"
FILE_NAME = "diabetes_prediction_dataset.csv"
FILE_PATH = os.path.join(DATA_DIR, FILE_NAME)

print("Kaggle dataset expected at:")
print(FILE_PATH)
print()
print("If you have the Kaggle API installed, use:")
print("kaggle datasets download -d iammustafatz/diabetes-prediction-dataset -p data")
print()
print("Then unzip the downloaded file into data/ and confirm the CSV is present:")
print(os.path.abspath(FILE_PATH))
