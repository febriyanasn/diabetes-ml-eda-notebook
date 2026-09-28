# Diabetes ML Project (Kaggle Dataset)

This project has been updated to use the Kaggle diabetes prediction dataset instead of the older BRFSS 2015 file.

## Dataset used

Dataset:
https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset/data

The CSV file is usually named something like:
- `diabetes_prediction_dataset.csv`

## Recommended location

Place the dataset in a local `data/` folder:

```bash
mkdir -p data
```

Then copy the Kaggle file into:

```bash
data/diabetes_prediction_dataset.csv
```

## How to run

1. Download the Kaggle file manually or via Kaggle API.
2. Save it to `data/diabetes_prediction_dataset.csv`.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open the notebook:

```bash
jupyter notebook diabetes_kaggle_eda_modeling_results.ipynb
```

## Project purpose

This project demonstrates:

- EDA for a diabetes prediction dataset
- target distribution analysis and class imbalance checks
- exploratory visualizations
- preprocessing and modeling pipeline
- classification metrics, confusion matrix, and ROC-AUC
- interpretation of model findings

## Important note

This repository does not include the Kaggle dataset file itself due to licensing and size considerations. You must download it from Kaggle and place it in `data/` before running the notebook.

## Notebook available

- `diabetes_kaggle_eda_modeling_results.ipynb`
