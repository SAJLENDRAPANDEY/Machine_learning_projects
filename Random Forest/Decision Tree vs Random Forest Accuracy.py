import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# ==============================
# 1. Load Dataset
# ==============================
data = pd.read_excel(r"C:\Users\SAJLE\Downloads\random_forest_dataset.xlsx")

# ==============================
# 2. Data Preprocessing
# ==============================
data = pd.get_dummies(data, columns=['Education_Level', 'City'], drop_first=True)

X = data.drop("Target", axis=1)
y = data["Target"]

# ==============================
# 3. Train-Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# 4. Decision Tree Model
# ==============================
dt_model = DecisionTreeClassifier(max_depth=3)
dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)

# ==============================
# 5. Random Forest Model
# ==============================
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

# ==============================
# 6. Visualization (Decision Tree)
# ==============================
plt.figure(figsize=(12, 8))
plot_tree(dt_model, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.title("Decision Tree Visualization")
plt.show()

# ==============================
# 7. Model Evaluation
# ==============================
print("\n===== MODEL PERFORMANCE =====")

print("\nAccuracy Score of Decision Tree is :", accuracy_score(y_test, y_pred_dt))
print("Accuracy Score of Random Forest is :", accuracy_score(y_test, y_pred_rf))

print("\nDecision Tree Confusion Matrix:\n", confusion_matrix(y_test, y_pred_dt))
print("\nRandom Forest Confusion Matrix:\n", confusion_matrix(y_test, y_pred_rf))
