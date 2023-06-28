import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pickle
import joblib

salaries = pd.read_csv('../data/nba_contracts_history.csv')

salaries = salaries.drop(
    columns=['GP', 'W', 'L', 'CONTRACT_END', 'OREB', 'DREB', '+/-', 'NAME', 'FG%', '3P%', 'FT%'])

print(salaries.columns)
salaries['CONTRACT_START'] = salaries['CONTRACT_START']-2011

target_salaries = salaries['AVG_SALARY']
features_salaries = salaries.drop(columns=['AVG_SALARY'])


x_train, x_test, y_train, y_test = train_test_split(
    features_salaries, target_salaries, random_state=40)

x_train = x_train.values
x_test = x_test.values
y_train = y_train.values
y_test = y_test.values


scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

print(x_train)
print(x_train.shape)
print('----')
print(x_test)
print(x_test.shape)

print(scaler.transform(np.array([4, 30, 2000, 1000, 400,
      850, 100, 300, 100, 150, 180, 100, 80, 40, 20, 200]).reshape(1, -1)))
with open('x_train.pkl', 'wb') as f:
    pickle.dump(x_train, f)

with open('x_test.pkl', 'wb') as f:
    pickle.dump(x_test, f)

with open('y_train.pkl', 'wb') as f:
    pickle.dump(y_train, f)

with open('y_test.pkl', 'wb') as f:
    pickle.dump(y_test, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
