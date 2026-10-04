# Diabetes Prediction with Machine Learning

> Educational ML demonstration comparing Logistic Regression and Random Forest through a FastAPI + React application.

## Overview

The application accepts eight numeric features from the Pima Indians Diabetes dataset and returns predictions from two trained scikit-learn classifiers.

This repository is intended for **learning and model-comparison purposes**. It is not a medical device, diagnostic system, or clinically validated prediction service.

## Dataset

The model code expects the **Pima Indians Diabetes** dataset with 768 rows, 8 predictor variables, and a binary outcome.

At startup, the backend downloads the CSV from a GitHub-hosted copy of the dataset:

```text
https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv
```

No local database is required for the training data, but backend startup therefore depends on access to that URL.

### Input features

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

## Models

### Logistic Regression

Used as the simpler, interpretable baseline. Features are standardized with `StandardScaler` fitted only on the training split.

### Random Forest

Used as the tree-based comparison model with 100 estimators and a fixed random seed.

## Reported evaluation

The README reports the current holdout results from a single **stratified 80/20 split** with `random_state=42`:

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.7143 | 0.6087 | 0.5185 | 0.5600 | 0.8230 |
| Random Forest | 0.7597 | 0.6809 | 0.5926 | 0.6337 | 0.8147 |

These are demonstration metrics for that single split. They should not be treated as a general estimate of clinical performance.

The current preprocessing does not perform clinical missing-value imputation or external validation, and the dataset's zero-valued measurements are used as numeric inputs.

## API

Backend endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/` | API root response |
| GET | `/api/models/metrics` | Return stored holdout metrics |
| POST | `/api/predict` | Run both models on validated input |

Example request:

```json
{
  "pregnancies": 6,
  "glucose": 148,
  "blood_pressure": 72,
  "skin_thickness": 35,
  "insulin": 0,
  "bmi": 33.6,
  "diabetes_pedigree_function": 0.627,
  "age": 50
}
```

The API enforces numeric bounds before inference and returns predictions plus class probabilities for both models.

## Frontend

The frontend is a React application built with the repository's CRA/CRACO toolchain. It displays model metrics, collects feature values, and calls the FastAPI backend.

## Run locally

### Backend

```bash
cd backend
python -m pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend

```bash
cd frontend
yarn install
yarn start
```

By default:

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8001`
- API docs: `http://localhost:8001/docs`

The backend's CORS configuration defaults to `http://localhost:3000` and can be overridden with `CORS_ORIGINS`.

## Validation and testing

A lightweight backend test validates accepted input and rejects an out-of-range age. GitHub Actions also runs the repository's automated checks.

This is not a substitute for a full ML evaluation pipeline, clinical validation, or production monitoring.

## Project structure

```text
Diabetes-Prediction-ML/
├── backend/
├── frontend/
├── .github/
├── LICENSE
└── README.md
```

## License

See [LICENSE](LICENSE).
