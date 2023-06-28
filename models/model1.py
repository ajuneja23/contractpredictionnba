import pickle
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


with open('x_train.pkl', 'rb') as f:
    x_train = pickle.load(f)

with open('x_test.pkl', 'rb') as f:
    x_test = pickle.load(f)

with open('y_train.pkl', 'rb') as f:
    y_train = pickle.load(f)
with open('y_test.pkl', 'rb') as f:
    y_test = pickle.load(f)


svr = SVR(kernel='linear')

svr.fit(x_train, y_train)

y_pred = svr.predict(x_test)

print('R^2 VALUE:')
print(r2_score(y_test, y_pred))

plt.scatter(y_pred, y_test, color='darkorange', label='data')
plt.legend()
plt.show()
plt.savefig('svr.png')
