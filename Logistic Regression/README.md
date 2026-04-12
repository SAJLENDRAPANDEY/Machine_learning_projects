
# ❤️ Heart Disease Prediction using Logistic Regression

## 📌 Project Overview

This project aims to predict the likelihood of heart disease using **Logistic Regression**, a popular machine learning algorithm for binary classification.
The model analyzes various health-related features and predicts whether a patient is likely to have heart disease or not.

---

## 🎯 Objectives

* Build a classification model using Logistic Regression
* Compare model performance **with and without feature scaling**
* Use a **pipeline** to improve workflow and avoid data leakage
* Evaluate the model using multiple performance metrics
* Visualize results using plots and heatmaps

---

## 📂 Dataset

* The dataset contains medical attributes such as:

  * Age
  * Sex
  * Chest Pain Type
  * Blood Pressure
  * Cholesterol
  * Heart Rate
  * And other health indicators

👉 Target Variable:

* `0` → No Heart Disease
* `1` → Heart Disease

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing

   * Handling missing values
   * Encoding categorical variables
3. Feature Selection
4. Train-Test Split
5. Model Training

   * Logistic Regression (with & without scaling)
6. Model Evaluation

   * Accuracy
   * Precision
   * Recall
   * F1-score
   * Confusion Matrix
7. Visualization

   * Heatmap
   * Scatter Plot
   * ROC Curve

---

## 📊 Model Evaluation

* Compared performance:

  * Without Scaling
  * With Scaling
  * Using Pipeline

* Metrics Used:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report
  * ROC Curve (AUC)

---

## 📈 Key Insights

* Feature scaling improves model performance
* Logistic Regression performs well for binary classification problems
* Recall is an important metric in healthcare-related predictions

---

## 📸 Visualizations

* Confusion Matrix Heatmap
* ROC Curve
* Scatter Plot (Age vs Heart Disease)

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
```

2. Navigate to the project folder:

```bash
cd heart-disease-prediction
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the project:

```bash
python model.py
```

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── data.csv
├── model.py
├── requirements.txt
├── README.md
└── outputs/
```

---

## 💡 Future Improvements

* Use advanced models (Decision Tree, Random Forest)
* Hyperparameter tuning
* Deploy using Streamlit or Flask
* Add real-time prediction interface

---

## 👨‍💻 Author

**Sajlendra Pandey**

* GitHub: https://github.com/SAJLENDRAPANDEY
* LinkedIn: https://www.linkedin.com/in/sajlendra-pandey-37378627b/

---

## ⭐ If you found this project useful, don't forget to star the repo!
