# 🌳 Decision Tree Classification Project

## 📌 Project Overview

This project demonstrates the implementation of a **Decision Tree Classifier** using Python and Scikit-learn to predict whether a student will **pass or not** based on various features.

The project covers the complete Machine Learning pipeline:

* Data preprocessing
* Model training
* Evaluation
* Visualization

---

## 🎯 Problem Statement

To build a machine learning model that predicts whether a student will **pass (Yes/No)** based on input features such as academic and behavioral attributes.

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* Scikit-learn
* Matplotlib

---

## 📂 Dataset

* The dataset is loaded from a local Excel file:

  ```
  decision_tree_dataset.xlsx
  ```
* Some unnecessary columns were removed:

  * Participation
  * Extra_Classes
  * Parent_Education

---

## ⚙️ Model Used

* **Decision Tree Classifier**
* Key parameter:

  ```
  max_depth = 2
  ```

---

## 🔄 Workflow

1. Load dataset
2. Data preprocessing
3. Encode target variable (Yes → 1, No → 0)
4. Split data into training and testing sets
5. Train Decision Tree model
6. Make predictions
7. Evaluate model performance
8. Visualize the decision tree

---

## 📊 Model Evaluation

### ✅ Accuracy

* The model performance is evaluated using accuracy score.

### 📌 Confusion Matrix

* Helps understand correct and incorrect predictions:

  * True Positive (TP)
  * True Negative (TN)
  * False Positive (FP)
  * False Negative (FN)

### 📌 Classification Report

Includes:

* Precision
* Recall
* F1-score

---

## 🌳 Decision Tree Visualization

* The decision tree is visualized using `plot_tree()` from Scikit-learn.
* It shows:

  * Feature splits
  * Gini impurity
  * Number of samples
  * Class distribution

---

## 🚀 Key Learnings

* Understanding of Decision Tree algorithm
* Importance of feature selection
* Model evaluation techniques
* Overfitting control using `max_depth`
* Visualization of ML models

---

## ⚠️ Limitations

* Model may overfit if tree depth is too large
* Performance depends on dataset quality

---

## 🔮 Future Improvements

* Hyperparameter tuning using GridSearchCV
* Use of Random Forest for better performance
* Cross-validation
* Feature engineering

---

## 📌 How to Run the Project

1. Install dependencies:

   ```
   pip install pandas scikit-learn matplotlib
   ```

2. Run the script:

   ```
   python main.py
   ```

---

## 👨‍💻 Author

**Sajlendra Pandey**

* GitHub: https://github.com/SAJLENDRAPANDEY
* LinkedIn: https://www.linkedin.com/in/sajlendra-pandey-37378627b/

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
