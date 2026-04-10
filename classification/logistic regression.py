"""
Logistic Regression Project
Author: Sajlendra Pandey

Description:
This project predicts whether a user will purchase a product
based on Age and Salary using Logistic Regression.
"""

# =========================
# 📦 Import Libraries
# =========================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# =========================
# 📊 Load Dataset
# =========================
def load_data():
    # Update path if needed
    data = pd.read_excel("data/logistic_regression_dataset.xlsx")
    return data


# =========================
# 🔍 Prepare Data
# =========================
def prepare_data(data):
    X = data[['Age', 'Salary']]
    y = data['Purchased']
    return train_test_split(X, y, test_size=0.2, random_state=2)


# =========================
# 🤖 Train Model
# =========================
def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


# =========================
# 🎯 Predict Function
# =========================
def predict_user(model):
    age = int(input("Enter Age: "))
    salary = int(input("Enter Salary: "))

    new_data = pd.DataFrame({
        'Age': [age],
        'Salary': [salary]
    })

    prediction = model.predict(new_data)

    if prediction[0] == 1:
        print("✅ User will purchase")
    else:
        print("❌ User will not purchase")


# =========================
# 📈 Evaluate Model
# =========================
def evaluate_model(model, X_test, y_test):
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")


# =========================
# 🚀 Main Function
# =========================
def main():
    data = load_data()
    X_train, X_test, y_train, y_test = prepare_data(data)

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)
    predict_user(model)


# =========================
# ▶️ Run Program
# =========================
if __name__ == "__main__":
    main()
