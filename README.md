# Diabetes Prediction Analysis Experiment

This project is a focused personal analysis experiment on diabetes classification using the Kaggle Diabetes Prediction Dataset. The objective is to test whether health and lifestyle indicators can predict whether a person has diabetes.

## Objective

Explore the relationship between demographic, physiological, and health-risk variables and diabetes status. The study uses a binary classification workflow to evaluate predictive performance and interpret the model outcomes.

## Dataset

Source:
https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data

Expected local file:
```bash
data/diabetes_prediction_dataset.csv
```

## Workflow

- data inspection and profiling
- missing value and duplicate checks
- target distribution analysis
- exploratory data analysis on key factors
- feature relationship analysis
- preprocessing pipeline
- model training and comparison
- evaluation using relevant classification metrics
- final interpretation and conclusions

## Notebook

- `diabetes_kaggle_eda_modeling_results.ipynb`

## Requirements

```bash
pip install -r requirements.txt
```

## Run the project

```bash
jupyter notebook diabetes_kaggle_eda_modeling_results.ipynb
```

## Summary

This experiment demonstrates how a health dataset can be turned into a classification problem and evaluated in a structured, reproducible way. It emphasizes both predictive modeling and careful interpretation, especially when dealing with class imbalance and healthcare-related outcomes.
