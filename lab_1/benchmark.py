import numpy as np
import timeit
import matplotlib.pyplot as plt
import seaborn as sns
from main import min_matrix


def generate_matrix(size: int) -> np.ndarray:
    return np.random.rand(size, size)


def benchmark():
    sizes = [2 ** i for i in range(13)]
    results = []
    for size in sizes:
        matrix = generate_matrix(size)
        time_taken = timeit.timeit(lambda: min_matrix(matrix), number=1)
        results.append((size, time_taken))
    return results


if __name__ == "__main__":
    sns.set(style="whitegrid")
    results = benchmark()
    sizes, times = zip(*results)
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o')
    plt.xscale('log', base=2)
    plt.yscale('log')
    plt.title('Execution Time of min_matrix Function for Different Matrix Sizes')
    plt.xlabel('Matrix Size (n x n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True, which="both", ls="--")
    plt.show()
