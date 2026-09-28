# Diabetes Prediction Analysis Experiment

This project is designed as a personal data science experiment focused on diabetes prediction using the Kaggle Diabetes Prediction Dataset.

## Objective

The purpose of this experiment is to explore whether a set of health and lifestyle indicators can accurately classify whether a person has diabetes or not. The project covers:

- data inspection and profiling
- missing-value and shape checks
- target distribution analysis
- exploratory data analysis (EDA)
- feature relationship analysis
- model selection and evaluation
- interpretation of the results

## Dataset

Dataset source:
https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data

The dataset is stored locally as:

```bash
data/diabetes_prediction_dataset.csv
```

## Why this dataset

This dataset is a strong choice for a machine learning experiment because it is:

- compact and clean
- tabular and easy to understand
- suitable for binary classification
- rich in medically meaningful features such as age, BMI, blood glucose, HbA1c level, hypertension, heart disease, and smoking history

## Project workflow

The analysis follows a standard machine learning workflow:

1. Load the dataset
2. Perform exploratory data analysis
3. Check data quality and distribution
4. Examine target imbalance
5. Investigate risk-related features
6. Build preprocessing pipelines
7. Train multiple classification models
8. Evaluate on the test set
9. Compare results and interpret findings

## Files in this repository

- `diabetes_kaggle_eda_modeling_results.ipynb` — end-to-end analysis notebook
- `download_kaggle_data.py` — helper script with Kaggle download instructions
- `requirements.txt` — Python dependencies for the project
- `README.md` — project documentation

## Dependencies

Install required packages with:

```bash
pip install -r requirements.txt
```

## How to run

1. Download the Kaggle dataset and save it as:

```bash
data/diabetes_prediction_dataset.csv
```

2. Open the notebook:

```bash
jupyter notebook diabetes_kaggle_eda_modeling_results.ipynb
```

## Analysis experiment summary

This experiment is intended as a structured learning project to understand how a practical diabetes classification pipeline behaves on a real-world health dataset. The goal is not only to achieve high accuracy, but also to examine:

- which features are most informative
- how the target is distributed
- whether class imbalance affects model quality
- which classification metrics are most meaningful
- how interpretable the trained models are

## Notes

This project is a personal analysis experiment and was designed to be educational and reproducible. It uses the Kaggle dataset as the primary source of analysis and does not depend on any external proprietary system.

## Suggested research question

Can health and lifestyle variables such as age, BMI, blood glucose, HbA1c level, and cardiovascular risk indicators be used to accurately classify whether a person has diabetes?
