# test_model.py
import numpy as np
from model import train_model

def test_train_model():
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])
    model = train_model(X, y)
    assert model is not None
    assert model.predict(X).shape == (4,)