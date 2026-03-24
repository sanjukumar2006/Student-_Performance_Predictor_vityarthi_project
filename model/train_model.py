import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('../data/students.csv')

X = data[['study_hours','attendance','previous_marks','assignments','internal_test']]
y = data['final_marks']

model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open('model.pkl','wb'))

print("Model trained and saved!")