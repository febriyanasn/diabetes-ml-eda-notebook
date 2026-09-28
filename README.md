# Diabetes + Social Media Integration Project

This project combines two analyses:

1. Diabetes classification using structured health indicators.
2. Social media text analysis to understand public discussions related to diabetes, symptoms, prevention, and support.

The notebook is designed as a practical learning project and demonstrates an ethically responsible workflow. It uses a health dataset for classification and a synthetic social-media-style dataset to illustrate how text analysis can be integrated into the project.

## What is included

- `diabetes_social_media_integration.ipynb`
- Structured diabetes classification using health variables
- Social text analysis for diabetes-related posts
- Simple NLP pipeline for topic and sentiment analysis
- Aggregated comparison of findings between the two data sources

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
jupyter notebook
```

Open `diabetes_social_media_integration.ipynb`.

## Important note

This project demonstrates the structure of a real integration workflow. In practice, if you want to use actual social media data, you must:

- use public and legally collected data only,
- avoid identifying individuals,
- respect platform terms of service,
- handle sensitive health information carefully,
- use aggregated analysis instead of linking personal data to medical records unless consent and legal basis exist.
