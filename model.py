# model.py
import numpy as np
from sklearn.linear_model import LogisticRegression

def train_model(x, y):
    model = LogisticRegression()
    model.fit(x, y)
    return model

if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    Y = np.array([0, 0, 1, 1])
    model = train_model(X, Y)
    print("Model trained.")