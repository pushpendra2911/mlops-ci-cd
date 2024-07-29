"""
Module test_model
"""

import numpy as np
from model import train_model

def test_train_model():
    """
    Test the train_model function.
    """
    x = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y = np.array([0, 0, 1, 1])
    model = train_model(x, y)
    assert model is not None
    assert model.predict(x).shape == (4,)

if __name__ == "__main__":
    test_train_model()
    print("All tests passed.")
