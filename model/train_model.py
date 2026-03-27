import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# data path (hardcoded… will change later if needed)

path = (r'E:\Sanju\VIT college\sem 2\AI and ml\vityarthi_project\data\student.csv')
data = pd.read_csv(path)

# selecting features manually (clearer than auto-select for debugging)

cols = ['study_hours', 'attendance', 'previous_marks', 'assignments', 'internal_test']
X = data[cols]

#  target column

y = data['final_marks']

# create model

reg = LinearRegression()

# fit model

reg.fit(X, y)

# save model

Save = (r'E:\Sanju\VIT college\sem 2\AI and ml\vityarthi_project\model\model.pkl')

file = open(Save, 'wb')
pickle.dump(reg, file)
file.close()

print("Model trained and saved!")