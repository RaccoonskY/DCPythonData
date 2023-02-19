import random
import numpy as np

random.seed(42)


class Perceptron:

    def __init__(self, num_features, nu, t_max):
        self.num_features = num_features
        self.nu = nu
        self.t_max = t_max

        self.w = np.zeros(self.num_features)
        self.b = 0

    def fit(self, X, y):
        t = 0
        while t <= self.t_max:
            r_index = random.randint(0, len(X) - 1)
            Xi, yi = X[r_index], y[r_index]
            if yi * self.predict(Xi) <= 0:
                self.b += self.nu * yi
                self.w += self.nu * yi * Xi
            t += 1

    def predict(self, X):
        X = np.atleast_2d(X)
        y = np.zeros(X.shape[0])

        for i in range(X.shape[0]):
            if sum(self.w * X[i, :]) + self.b >= 0:
                y[i] = +1
            else:
                y[i] = -1
        return y