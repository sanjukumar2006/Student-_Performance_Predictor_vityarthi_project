import pickle

# Load trained model
model = pickle.load(open(r'E:\Sanju\VIT college\sem 2\AI and ml\vityarthi_project\model\model.pkl','rb'))

# Take input from user
study = float(input("Study hours:"))
attend = float(input("Attendance:"))
previous = float(input("Previous marks:"))
assign = float(input("Assignment completion:"))
internal = float(input("Internal score:"))

# Prediction
prediction = model.predict([[study, attend, previous, assign, internal]])

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