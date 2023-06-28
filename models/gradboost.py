import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

with open('x_train.pkl', 'rb') as f:
    x_train = pickle.load(f)

with open('x_test.pkl', 'rb') as f:
    x_test = pickle.load(f)

with open('y_train.pkl', 'rb') as f:
    y_train = pickle.load(f)
with open('y_test.pkl', 'rb') as f:
    y_test = pickle.load(f)


print(x_train)
model = GradientBoostingRegressor(n_estimators=250, learning_rate=0.22)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print('R^2 score:')
print(r2_score(y_test, y_pred))  # 0.48
