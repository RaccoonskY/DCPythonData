import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from perception import Perceptron

X, y = load_iris(return_X_y=True)
X, y = X[:100], y[:100]
num_features = X.shape[1]

y = np.array([1 if y_i == 1 else -1 for y_i in y])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=10)
model = Perceptron(num_features, 0.1, 40)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = round(accuracy_score(y_test, y_pred), 2)
print("score {0:.2f}".format(score))



