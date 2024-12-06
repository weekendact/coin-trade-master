import lightgbm as lgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

import lightgbm as lgb

def train_lightgbm(X_train, y_train, X_val, y_val):
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)

    params = {
        "objective": "multiclass",
        "num_class": 3,  # 클래스 개수 (-1, 0, 1 → 0, 1, 2)
        "metric": "multi_logloss",
        "boosting_type": "gbdt",
        "learning_rate": 0.05,
        "num_leaves": 31,
        "max_depth": -1,
        "verbose": -1,
    }

    print("Training model...")
    model = lgb.train(
        params=params,
        train_set=train_data,
        valid_sets=[train_data, val_data],
        valid_names=["train", "validation"],
        num_boost_round=1000,
        callbacks=[lgb.early_stopping(stopping_rounds=10)]  # 콜백으로 early stopping 설정
    )

    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the test set and return metrics.
    """
    print("Generating predictions...")
    predictions = model.predict(X_test)
    predicted_classes = predictions.argmax(axis=1) if predictions.ndim > 1 else (predictions > 0.5).astype(int)

    print("\nCalculating metrics...")
    metrics = {
        "accuracy": accuracy_score(y_test, predicted_classes),
        "precision_macro": precision_score(y_test, predicted_classes, average="macro", zero_division=0),
        "recall_macro": recall_score(y_test, predicted_classes, average="macro", zero_division=0),
        "f1_macro": f1_score(y_test, predicted_classes, average="macro", zero_division=0),
    }

    print("\nMetrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predicted_classes, zero_division=0))

    return metrics