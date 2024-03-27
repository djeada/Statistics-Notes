from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

def generate_data(n_samples: int, n_features: int, random_state: int) -> tuple:
    """Generates a synthetic dataset for classification.

    Args:
        n_samples (int): Number of samples.
        n_features (int): Number of features.
        random_state (int): Random state for reproducibility.

    Returns:
        tuple: Feature matrix (X) and target vector (y).
    """
    return make_classification(n_samples=n_samples, n_features=n_features, 
                               n_informative=2, n_redundant=0, random_state=random_state)

def split_data(X, y, test_size: float, random_state: int) -> tuple:
    """Splits data into training and test sets.

    Args:
        X: Feature matrix.
        y: Target vector.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random state for reproducibility.

    Returns:
        tuple: Split data into training and test sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def fit_model(X_train, y_train) -> LogisticRegression:
    """Fits a Logistic Regression model to the training data.

    Args:
        X_train: Training feature matrix.
        y_train: Training target vector.

    Returns:
        LogisticRegression: Trained model.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def calculate_metrics(y_test, y_pred) -> tuple:
    """Calculates various classification metrics.

    Args:
        y_test: Actual target values.
        y_pred: Predicted target values.

    Returns:
        tuple: Confusion matrix, accuracy, precision, recall, and F1 score.
    """
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    return cm, accuracy, precision, recall, f1

def plot_results(X_test, y_test, y_pred) -> None:
    """Plots the classification results.

    Args:
        X_test: Test feature matrix.
        y_test: Actual target values.
        y_pred: Predicted target values.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', marker='o', label='Actual')
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis', marker='x', label='Predicted')
    plt.title('Classification Data (Actual vs. Predicted)')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

# Generate, split and train model on synthetic data
X, y = generate_data(200, 2, 42)
X_train, X_test, y_train, y_test = split_data(X, y, 0.25, 42)
model = fit_model(X_train, y_train)

# Make predictions and calculate metrics
y_pred = model.predict(X_test)
cm, accuracy, precision, recall, f1 = calculate_metrics(y_test, y_pred)

# Print the metrics
print("Confusion Matrix:\n", cm)
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Visualize the results
plot_results(X_test, y_test, y_pred)
