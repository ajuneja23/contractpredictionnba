from sklearn.ensemble import AdaBoostRegressor
import pickle
from sklearn.metrics import r2_score


with open('x_train.pkl', 'rb') as f:
    x_train = pickle.load(f)

with open('x_test.pkl', 'rb') as f:
    x_test = pickle.load(f)

with open('y_train.pkl', 'rb') as f:
    y_train = pickle.load(f)
with open('y_test.pkl', 'rb') as f:
    y_test = pickle.load(f)


regressor = AdaBoostRegressor(n_estimators=500, learning_rate=3)


regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

print('R2 Value:')
print(r2_score(y_test, y_pred))  # R^2: 0.54
