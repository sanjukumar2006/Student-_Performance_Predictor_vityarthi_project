import pickle

# Load trained model
model = pickle.load(open(r'E:\Sanju\VIT college\sem 2\AI and ml\vityarthi_project\model\model.pkl','rb'))

# Take input from user
study_hours = float(input("Study hours: "))
attendance = float(input("Attendance (%): "))
previous_marks = float(input("Previous marks: "))
assignments = float(input("Assignment completion (%): "))
internal_test = float(input("Internal test score: "))

# Prediction
prediction = model.predict([[study_hours, attendance, previous_marks, assignments, internal_test]])

marks = prediction[0]

# Performance category
if marks >= 80:
    category = "High"
elif marks >= 50:
    category = "Medium"
else:
    category = "Low"

print("\nPredicted Final Marks:", round(marks,2))
print("Performance:", category)