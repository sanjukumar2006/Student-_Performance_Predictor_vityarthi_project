# 🎓 Student Performance Predictor (AI/ML)

An AI-based system that predicts **student final exam performance** using machine learning. The model analyzes academic factors such as study hours, attendance, previous marks, assignments, and internal test scores to estimate final marks and performance category.

---

# 📌 Problem Statement

Teachers and students cannot easily identify who may perform poorly in exams. Academic performance depends on multiple factors:

* Study hours
* Attendance percentage
* Previous marks
* Assignment completion
* Internal test scores

This project builds a **machine learning model** to predict:

* Final marks
* Performance category (High / Medium / Low)

---

# 🎯 Solution

This system:

1. Loads student dataset
2. Trains a Linear Regression model
3. Saves trained model as `model.pkl`
4. Uses saved model to predict performance
5. Classifies performance into High / Medium / Low

---

# 🧠 Machine Learning Used

Model: **Linear Regression**
Library: **scikit-learn**

Why Linear Regression?

* Fast training
* Works well for marks prediction
* Simple and interpretable
* No GPU required

---

# 📂 Project Structure

```
vityarthi_project
│
├── data
│   └── student.csv
│
├── model
│   ├── train_model.py
│   └── model.pkl
│
├── prediction.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ How It Works

## Step 1 — Training Phase

`train_model.py`

* Reads dataset using pandas
* Splits input and output
* Trains Linear Regression model
* Saves model using pickle

Output file created:

```
model/model.pkl
```

This file contains trained AI model.

---

## Step 2 — Prediction Phase

`prediction.py`

* Loads model.pkl
* Takes user input
* Predicts final marks
* Classifies performance

---

# 📥 Inputs

The model uses 5 features:

| Feature        | Description             |
| -------------- | ----------------------- |
| study_hours    | Hours studied per day   |
| attendance     | Attendance percentage   |
| previous_marks | Previous exam marks     |
| assignments    | Assignment completion % |
| internal_test  | Internal test score     |

---

# 📤 Output

The system returns:

* Predicted Final Marks
* Performance Category

Categories:

* High → marks >= 80
* Medium → marks 50–79
* Low → marks < 50

---

# ▶️ How To Run

## 1 Install dependencies

```
pip install -r requirements.txt
```

---

## 2 Train Model

```
python model/train_model.py
```

Output:

```
Model trained and saved!
```

---

## 3 Run Prediction

```
python prediction.py
```

---

# 💡 Example

Input:

```
Study hours: 6
Attendance: 85
Previous marks: 70
Assignments: 75
Internal test: 72
```

Output:

```
Predicted Final Marks: 74.8
Performance: Medium
```

---

# 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Pickle

---

# 📈 Future Improvements

* Web dashboard
* Student risk detection
* Graph visualization
* CSV batch prediction
* Deep learning model
* Teacher analytics panel

---

# 👨‍💻 Author

Sanju Kumar

AI & ML Student Performance Predictor Project

---

# 🚀 What This Project Solves

✅ Predicts weak students early
✅ Helps teachers intervene
✅ Improves student performance
✅ Data-driven academic insights
✅ Automated performance evaluation

---

# 🔚 End
