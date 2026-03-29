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

## Training Phase

* Dataset is loaded using pandas
* Features and target selected
* Linear Regression model trained
* Model saved as `model.pkl`

## Prediction Phase

* Load saved model
* Take user inputs
* Predict final marks
* Classify performance

---

# 📥 Inputs

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

# 🧰 Dependencies

This project requires:

* Python 3.8 or higher
* pandas
* numpy
* scikit-learn

---

# ⚙️ Setup Instructions

## Step 1 — Download or Clone Project

Download the project folder:

```
vityarthi_project
```

---

## Step 2 — Install Dependencies

Open terminal in project folder and run:

```
pip install -r requirements.txt
```

This installs:

* pandas
* numpy
* scikit-learn

---

# ⚙️ Configuration Steps

No special configuration required.

Make sure following files exist:

Dataset:

```
data/student.csv
```

Training script:

```
model/train_model.py
```

Prediction script:

```
prediction.py
```

---

# ▶️ Execution Steps

## Step 1 — Train Model

Run:

```
python model/train_model.py
```

Output:

```
Model trained and saved!
```

This creates:

```
model/model.pkl
```

---

## Step 2 — Run Prediction

Run:

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

# 🧠 What This Project Does

This system:

* Predicts student final marks
* Classifies performance level
* Identifies weak students early
* Helps teachers take action
* Provides data-driven insights

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
Student Performance Predictor Project

---

# 🚀 What This Project Solves

✅ Predicts weak students early
✅ Helps teachers intervene
✅ Improves student performance
✅ Data-driven academic insights
✅ Automated performance evaluation

---
