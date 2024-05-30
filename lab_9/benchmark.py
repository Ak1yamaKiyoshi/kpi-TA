import time
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import numpy as np

def shell_sort(ship_list):
    n = len(ship_list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = ship_list[i]
            j = i
            while j >= gap and ship_list[j - gap].num_matroses > temp.num_matroses:
                ship_list[j] = ship_list[j - gap]
                j -= gap
            ship_list[j] = temp
        gap //= 2


def bubble_sort(ship_list):
    n = len(ship_list)

    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            
            if ship_list[j].num_matroses > ship_list[j + 1].num_matroses:
                flag = True
                ship_list[j], ship_list[j + 1] = ship_list[j + 1], ship_list[j]
        if not flag:break


def counting_sort(ship_list):
    if not ship_list:
        return []  # Return an empty list if the input is empty

    max_matroses = max(ship.num_matroses for ship in ship_list)
    counts = [0] * (max_matroses + 1)
    for ship in ship_list:
        counts[ship.num_matroses] += 1
    sorted_ships = []
    for i in range(len(counts)):
        sorted_ships.extend([Ship(i)] * counts[i])
    ship_list[:] = sorted_ships


class Ship:
    def __init__(self, num_matroses):
        self.num_matroses = num_matroses

    def __str__(self):
        return f"Ship with {self.num_matroses} matroses"


# Function to measure time taken by a sorting algorithm
def measure_time(func, ship_list):
    start_time = time.time()
    func(ship_list)
    end_time = time.time()
    return end_time - start_time


# Benchmarking function for Sorting Algorithms
def benchmark_sorting(sorting_func, ship_list_sizes, num_similar_levels):
    results = []
    for size in tqdm(ship_list_sizes):
        for similar_level in num_similar_levels:
            for case in ['half_sorted', 'unsorted', 'reversed']:
                ship_list = generate_ship_list(size, case, similar_level)
                sorting_time = measure_time(sorting_func, ship_list)
                results.append((size, similar_level, case, sorting_time))
    return results


# Function to generate ship lists with different cases
def generate_ship_list(size, case, num_similar):
    if size == 0:
        return []  # Return an empty list if the size is 0

    if case == 'half_sorted':
        unsorted_list = [Ship(random.randint(10, 10000)) for _ in range(size // 2)]
        sorted_list = sorted([Ship(random.randint(10, 10000)) for _ in range(size - size // 2)], key=lambda x: x.num_matroses)
        return unsorted_list + sorted_list
    elif case == 'unsorted':
        return [Ship(random.randint(10, 10000)) for _ in range(size)]
    elif case == 'reversed':
        return sorted([Ship(random.randint(10, 10000)) for _ in range(size)], key=lambda x: x.num_matroses, reverse=True)
    elif case == 'similar':
        if num_similar > size:
            num_similar = size
        random_val = random.randint(10, 10000)
        values = [random_val for _ in range(num_similar)]
        ships = []
        for v in values:
            ships.extend([Ship(v)] * (size // num_similar))
        ships.extend([Ship(random.randint(10, 10000)) for _ in range(size % num_similar)])
        
        return np.random.shuffle(ships)


# Function to plot benchmarking results
def plot_results(results, title, filename, sorting_func):
    plt.figure(figsize=(17, 4))
    sizes = sorted(set([r[0] for r in results]))
    similar_levels = set([r[1] for r in results])

    for case in ['half_sorted', 'unsorted', 'reversed']:
        plt.subplot(1, 3, ['half_sorted', 'unsorted', 'reversed'].index(case) + 1)
        plt.title(f"{case.replace('_', ' ').title()} Case")
        plt.xlabel("Ship List Size")
        plt.ylabel("Time (seconds)")

        for similar_level in similar_levels:
            times = [r[3] for r in results if r[0] in sizes and r[1] == similar_level and r[2] == case]
            plt.plot(sizes, times, label=f"Similar: {similar_level}", marker=',')

        plt.legend()

    plt.suptitle(f"{sorting_func.__name__.replace('_', ' ').title()} Sort Benchmark")
    plt.tight_layout()
    plt.savefig(f"images/{filename}")


if __name__ == "__main__":
    ship_list_sizes = [i * 5 for i in range(250)]  # [100, 500, 1000, 5000, 10000]  # Adjust the list sizes as needed
    num_similar_levels = [ 0, 500]
    # Benchmarking Bubble Sort
    bubble_sort_results = benchmark_sorting(bubble_sort, ship_list_sizes, num_similar_levels)
    plot_results(bubble_sort_results, "bubble_sort_benchmark.png", "bubble_sort_benchmark.png", bubble_sort)

    # Benchmarking Shell Sort
    shell_sort_results = benchmark_sorting(shell_sort, ship_list_sizes, num_similar_levels)
    plot_results(shell_sort_results, "shell_sort_benchmark.png", "shell_sort_benchmark.png", shell_sort)

    # Benchmarking Counting Sort
    counting_sort_results = benchmark_sorting(counting_sort, ship_list_sizes, num_similar_levels)
    plot_results(counting_sort_results, "counting_sort_benchmark.png", "counting_sort_benchmark.png", counting_sort)