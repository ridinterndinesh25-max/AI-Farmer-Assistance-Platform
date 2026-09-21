import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Crop_recommendation.csv"
)

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "crop_recommendation_model.pkl"
)


# Dataset load
data = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)


# Input features
X = data[
    [
        "N",
        "P",
        "K",
        "temperature",
        "humidity",
        "ph",
        "rainfall"
    ]
]

# Target
y = data["label"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Random Forest model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)


# Train
model.fit(X_train, y_train)


# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"Model Accuracy: {accuracy * 100:.2f}%")


# Save model
joblib.dump(
    model,
    MODEL_PATH
)

print("Model saved successfully!")
print(MODEL_PATH)