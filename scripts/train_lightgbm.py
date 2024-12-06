import pandas as pd
from imblearn.over_sampling import SMOTE
from src.models.lightgbm_model import train_lightgbm, evaluate_model

# Load data
print("Loading data...")
X_train = pd.read_csv("data/labeled/X_train_scaled.csv")
y_train = pd.read_csv("data/labeled/y_train.csv")
X_val = pd.read_csv("data/labeled/X_val_scaled.csv")
y_val = pd.read_csv("data/labeled/y_val.csv")
X_test = pd.read_csv("data/labeled/X_test_scaled.csv")
y_test = pd.read_csv("data/labeled/y_test.csv")

# Transform labels
label_mapping = {-1: 0, 0: 1, 1: 2}
y_train = y_train.replace(label_mapping)
y_val = y_val.replace(label_mapping)
y_test = y_test.replace(label_mapping)

# Balance data using SMOTE
print("Balancing data with SMOTE...")
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
print("Balanced class distribution:\n", y_train_balanced.value_counts())

# Train model
print("Training LightGBM model...")
model = train_lightgbm(X_train_balanced, y_train_balanced, X_val, y_val)

# Evaluate model
print("Evaluating model...")
metrics = evaluate_model(model, X_test, y_test)

# Print metrics
print("\nEvaluation Metrics:")
for metric, value in metrics.items():
    print(f"{metric}: {value:.4f}")
