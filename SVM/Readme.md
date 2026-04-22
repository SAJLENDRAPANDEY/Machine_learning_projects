# 📊 SVM Classification Project

## 🔹 Overview

This project uses a Support Vector Machine (SVM) model to classify data after preprocessing and feature scaling.

---

## ⚙️ Steps Performed

* Loaded dataset using Pandas
* Converted categorical features using one-hot encoding
* Split data into training and testing sets
* Applied feature scaling using StandardScaler
* Trained SVM model with:

  * `kernel = linear`
  * `class_weight = balanced`
* Evaluated model using accuracy and classification report

---

## 📈 Model Performance

### ✅ Accuracy

```
Accuracy Score: 0.80
```

---

### 📊 Classification Report

```
              precision    recall  f1-score   support

           0       0.56      0.84      0.67       242
           1       0.94      0.79      0.86       758

    accuracy                           0.80      1000
   macro avg       0.75      0.81      0.76      1000
weighted avg       0.85      0.80      0.81      1000
```

---

## 🔍 Key Insights

* The dataset is imbalanced (Class 1 > Class 0)
* Using `class_weight='balanced'` improved recall for minority class (Class 0)
* Model provides balanced performance across classes

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Seaborn & Matplotlib

---

## 🚀 Future Improvements

* Hyperparameter tuning (GridSearchCV)
* Compare with Random Forest & Logistic Regression
* Add confusion matrix visualization
* Deploy model using Streamlit or FastAPI

---
