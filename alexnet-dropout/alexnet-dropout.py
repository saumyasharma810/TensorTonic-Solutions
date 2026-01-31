import numpy as np

def dropout(x: np.ndarray, p: float = 0.5, training: bool = True) -> np.ndarray:
    """Apply dropout to input."""
    # YOUR CODE HERE
    if not training:
        return x
    y = 1/(1-p)
    out = x * y
    prob = np.random.rand(*x.shape)
    out2 = (prob>p).astype(int)
    out *= out2
    return out