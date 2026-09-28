# Diabetes EDA Notebook

This repository contains a beginner-friendly Jupyter notebook for Exploratory Data Analysis (EDA) on the CDC Diabetes Health Indicators dataset.

## Project goal

The notebook walks through a standard data science workflow:

- loading the dataset
- checking shape and dtypes
- cleaning and labeling categorical variables
- identifying missing values
- analyzing the target variable
- visualizing feature distributions
- comparing risk factors across diabetes status
- summarizing key findings before modeling

## How to run

1. Clone this repository.
2. Create a virtual environment (optional but recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open the notebook:

```bash
jupyter notebook diabetes_eda.ipynb
```

## Dataset

The notebook uses the CDC Diabetes Health Indicators dataset (`diabetes_binary_health_indicators_BRFSS2015.csv`), which contains health and lifestyle variables related to diabetes risk.

The analysis is inspired by the EDA workflow in the reference project: https://github.com/eviekenna/FinalProjectST558
