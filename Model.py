import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

data = pd.read_excel(r"C:\Users\cyndd\Downloads\hiring.xlsx")

x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

regressor = LinearRegression()
regressor.fit(x, y)

pickle.dump(regressor, open('model.pkl', 'wb'))
