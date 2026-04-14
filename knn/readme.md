# 🌸 KNN Iris Classification

A machine learning project that uses the **K-Nearest Neighbors (KNN)** algorithm to classify iris flowers into different species based on their physical features.

---

## 📌 Project Overview

This project builds a classification model that predicts the species of an iris flower using features like sepal length, sepal width, petal length, and petal width.

It demonstrates the complete machine learning workflow including data preprocessing, model training, evaluation, and prediction.

---

## 🚀 Features

* 📊 Data preprocessing using Pandas
* 🔀 Train-test split with stratification
* ⚖️ Feature scaling using StandardScaler
* 🔍 Hyperparameter tuning (optimal K selection)
* 🤖 Model training using KNN
* 📈 Accuracy evaluation
* 📉 Confusion Matrix analysis
* 🔮 Prediction on new input data

---

## 📊 Dataset

* Iris dataset (Excel format)
* Features:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width
* Target:

  * Species (Setosa, Versicolor, Virginica)

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## 🔍 Workflow

1. Load dataset
2. Split data into training and testing sets
3. Apply feature scaling
4. Train KNN model
5. Find optimal K value
6. Evaluate model performance
7. Make predictions on new data

---

## 📈 Model Performance

* Accuracy: ~100% (on Iris dataset)
* Balanced classification across all species

---

## 🔮 Example Prediction

**Input:**

```
[7, 3.2, 4.7, 1.4]
```

**Output:**

```
Versicolor
```

---

## 📌 How to Run

### 1. Clone the repository

```
git clone https://github.com/SAJLENDRAPANDEY/knn-iris-classification.git
```

### 2. Install dependencies

```
pip install pandas numpy scikit-learn matplotlib
```

### 3. Run the project

```
python knn_model.py
```

---

## 📂 Project Structure

```
knn-iris-classification/
│
├── data/
│   └── iris dataset.xlsx
│
├── knn_model.py
├── README.md
└── requirements.txt
```

---

## 💡 Future Improvements

* Build a Streamlit web app
* Deploy the model online
* Use larger real-world datasets

---

## 👤 Author

**Sajlendra Pandey**

* 🔗 GitHub: https://github.com/SAJLENDRAPANDEY
* 🔗 LinkedIn: https://www.linkedin.com/in/sajlendra-pandey-37378627b

---

## ⭐ If you found this useful

Give this repo a ⭐ and connect with me!
