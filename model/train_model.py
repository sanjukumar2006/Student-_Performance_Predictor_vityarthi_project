import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv(r'E:\Sanju\VIT college\sem 2\AI and ml\vityarthi_project\data\student.csv')

X = data[['study_hours','attendance','previous_marks','assignments','internal_test']]
y = data['final_marks']

model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open(r'E:\Sanju\VIT college\sem 2\AI and ml\vityarthi_project\model\model.pkl','wb'))

print("Model trained and saved!")