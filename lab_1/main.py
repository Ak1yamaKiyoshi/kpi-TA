import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional

"""
Пошук мінімального елемента (індекс і значення) в двомірному масиві з nm елементів.
"""


def min_matrix(matrix: np.ndarray) -> Tuple[
                            Optional[float], Tuple[
                                Optional[int], Optional[int]]]:
    if matrix.shape == (0,):
        return None, (None, None)
    least: Optional[float] = None
    pos: Optional[int, int] = (None, None)
    for i, column in enumerate(matrix):
        for j, element in enumerate(column):
            if not np.isnan(element) \
                    and (least is None or element < least):
                least, pos = element, (i, j)
    return least, pos


if __name__ == "__main__":
    cur: np.ndarray = np.random.rand(5, 5)
    print(cur)
    plt.imshow(cur)
    plt.show()
    print(min_matrix(cur))
