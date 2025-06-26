import numpy as np

def gaussian_elimination(A, b):
    """
    Solves a system of linear equations Ax = b using Gaussian elimination.

    Args:
        A (np.ndarray): The coefficient matrix.
        b (np.ndarray): The constant vector.

    Returns:
        np.ndarray: The solution vector x.
        None: If the matrix is singular (no unique solution).
    """
    n = len(b)
