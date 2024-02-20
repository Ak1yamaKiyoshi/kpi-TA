import pytest
from lab_1.main import min_matrix
import numpy as np


def test_min_matrix():
    matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert min_matrix(matrix_1) == (1, (0, 0))

    matrix_2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    assert min_matrix(matrix_2) == (1, (2, 2))

    matrix_3 = np.array([[1, 2], [3, 4]])
    assert min_matrix(matrix_3) == (1, (0, 0))

    matrix_4 = np.array([[0, 0], [0, 0]])
    assert min_matrix(matrix_4) == (0, (0, 0))

    matrix_5 = np.array([[5]])
    assert min_matrix(matrix_5) == (5, (0, 0))

    # Test case with negative numbers
    matrix_6 = np.array([[5, -3, 7], [-2, 0, 4], [-8, 9, 1]])
    assert min_matrix(matrix_6) == (-8, (2, 0))

    # Test case with float numbers
    matrix_7 = np.array([[1.5, 2.7, 3.9], [4.2, 5.1, 6.8], [7.3, 8.6, 9.4]])
    assert min_matrix(matrix_7) == (1.5, (0, 0))

    # Test case with NaN values
    matrix_8 = np.array([[np.nan, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert min_matrix(matrix_8) == (2, (0, 1))

    # Test case with all NaN values
    matrix_9 = np.array([[np.nan, np.nan], [np.nan, np.nan]])
    assert min_matrix(matrix_9) == (None, (None, None))

    # Test case with empty matrix
    matrix_10 = np.array([])
    assert min_matrix(matrix_10) == (None, (None, None))

if __name__ == "__main__":
    pytest.main()
