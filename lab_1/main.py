import json

import numpy as np
import matplotlib.pyplot as plt
import os
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

class Program:
    def __init__(self, n: int = 1, m: int = 1) -> None:
        self.matrix = np.zeros(shape=(n, m))
        self.cache_filename = './matrix_cache.dat'

    def from_file(self):
        try:
            with open(input('Enter filename: '), 'r+') as f:
                self.matrix = np.array(eval(f.read()))
        except Exception as e:
            print(f"Something gone wrong", e)

    def to_file(self):
        try:
            with open(input('Enter filename: '), 'w+') as f:
                f.write(str(self.matrix.tolist()))
        except Exception as e:
            print(f"Something gone wrong", e)


    def from_input(self):
        try:
            n, m = int(input("Enter columns: ")), int(input("Enter rows: "))
            self.__init__(n, m)
        except ValueError:
            print(" Invalid input, please try again ")
            self.from_input()
            return

        i, j = 0, 0
        while i < n:
            while j < m:
                try:
                    self.matrix[i][j] = float(input(f"[{i}][{j}]: "))
                    j += 1
                except ValueError:
                    print("You can enter only float numbers, try again")
            i += 1
            j = 0

    def from_random(self):
        try:
            n, m = int(input("Enter columns: ")), int(input("Enter rows: "))
            self.__init__(n, m)
        except ValueError:
            print(" Invalid input, please try again ")
            self.from_random()
            return
        n, m = self.matrix.shape
        self.matrix = np.random.rand(n, m)

    def menu(self):
        #try:
        [self.from_file, self.from_input, self.from_random][int(input("""Choose how to fill the matrix:
1. From file 
2. From input
3. From random
"""))-1]()

        print(f"> Matrix: \n {self.matrix}")
        min_num = min_matrix(self.matrix)
        print(f"> Min number of matrix {min_num[0]} with coordinates {min_num[1]}")
        if input("Save matrix? y/n").startswith('y'):
            self.to_file()


if __name__ == "__main__":
    Program().menu()