# 📦 Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report


# 📂 Load Dataset
data = pd.read_excel(r"C:\Users\SAJLE\Downloads\random_forest_dataset.xlsx")


# 🧹 Data Preprocessing
data = pd.get_dummies(data, columns=["Education_Level", "City"], drop_first=True)

X = data.drop("Target", axis=1)
y = data["Target"]


# 🔀 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 📏 Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 🤖 Model Training
model = SVC(class_weight='balanced', kernel='linear')
model.fit(X_train, y_train)


# 🔮 Prediction
y_pred = model.predict(X_test)


# 📊 Evaluation
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
