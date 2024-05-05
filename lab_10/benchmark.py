import time
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import numpy as np


def heapsort(ship_list, low, high):
    def heapify(ship_list, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and ship_list[l] > ship_list[largest]:
            largest = l

        if r < n and ship_list[r] > ship_list[largest]:
            largest = r

        if largest != i:
            ship_list[i], ship_list[largest] = ship_list[largest], ship_list[i]
            heapify(ship_list, n, largest)

    n = len(ship_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(ship_list, n, i)

    for i in range(n - 1, 0, -1):
        ship_list[i], ship_list[0] = ship_list[0], ship_list[i]
        heapify(ship_list, i, 0)

class Ship:
    def __init__(self, num_matroses):
        self.num_matroses = num_matroses

    def __str__(self):
        return f"Ship with {self.num_matroses} matroses"

    def __lt__(self, other):
        return self.num_matroses < other.num_matroses

    def __le__(self, other):
        return self.num_matroses <= other.num_matroses

    def __gt__(self, other):
        return self.num_matroses > other.num_matroses

    def __ge__(self, other):
        return self.num_matroses >= other.num_matroses




def quicksort_standard(ship_list, low, high):
    if low < high:
        pivot = ship_list[high]
        i = low - 1
        for j in range(low, high):
            if ship_list[j] < pivot:
                i += 1
                ship_list[i], ship_list[j] = ship_list[j], ship_list[i]
        ship_list[i + 1], ship_list[high] = ship_list[high], ship_list[i + 1]
        pivot_index = i + 1
        quicksort_standard(ship_list, low, pivot_index - 1)
        quicksort_standard(ship_list, pivot_index + 1, high)

def quicksort_improved_pivot(ship_list, low, high):
    if low < high:
        pivot = ship_list[high]
        i = low - 1
        for j in range(low, high):
            if ship_list[j] < pivot:
                i += 1
                ship_list[i], ship_list[j] = ship_list[j], ship_list[i]
        ship_list[i + 1], ship_list[high] = ship_list[high], ship_list[i + 1]
        pivot_index = i + 1
        quicksort_improved_pivot(ship_list, low, pivot_index - 1)
        quicksort_improved_pivot(ship_list, pivot_index + 1, high)

def quicksort_random_pivot(ship_list, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        ship_list[pivot_index], ship_list[high] = ship_list[high], ship_list[pivot_index]
        pivot = ship_list[high]
        i = low - 1
        for j in range(low, high):
            if ship_list[j] < pivot:
                i += 1
                ship_list[i], ship_list[j] = ship_list[j], ship_list[i]
        ship_list[i + 1], ship_list[high] = ship_list[high], ship_list[i + 1]
        pivot_index = i + 1
        quicksort_random_pivot(ship_list, low, pivot_index - 1)
        quicksort_random_pivot(ship_list, pivot_index + 1, high)

def quicksort_three_way(ship_list, low, high):
    if low < high:
        pivot = ship_list[high]
        i = low
        while i <= high:
            if ship_list[i] < pivot:
                ship_list[i], ship_list[low] = ship_list[low], ship_list[i]
                low += 1
                i += 1
            elif ship_list[i] == pivot:
                i += 1
            else:
                ship_list[i], ship_list[high] = ship_list[high], ship_list[i]
                high -= 1
        quicksort_three_way(ship_list, low, high - 1)
        quicksort_three_way(ship_list, high + 1, high)

def introsort(ship_list, low, high, max_depth=None):
    if max_depth is None:
        max_depth = 2 * (high - low + 1).bit_length()

    if low < high:
        if max_depth == 0:
            heapsort(ship_list, low, high)
        else:
            pivot_index = random.randint(low, high)
            ship_list[pivot_index], ship_list[high] = ship_list[high], ship_list[pivot_index]
            pivot = ship_list[high]
            i = low - 1
            for j in range(low, high):
                if ship_list[j] <= pivot:
                    i += 1
                    ship_list[i], ship_list[j] = ship_list[j], ship_list[i]
            ship_list[i + 1], ship_list[high] = ship_list[high], ship_list[i + 1]
            pivot_index = i + 1
            introsort(ship_list, low, pivot_index - 1, max_depth - 1)
            introsort(ship_list, pivot_index + 1, high, max_depth - 1)

def optimized_quicksort(ship_list, low, high):
    while low < high:
        if high - low > 16:
            pivot = ship_list[high]
            i = low - 1
            j = high
            while True:
                i += 1
                while ship_list[i] < pivot:
                    i += 1
                j -= 1
                while ship_list[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                ship_list[i], ship_list[j] = ship_list[j], ship_list[i]
            ship_list[i], ship_list[high] = ship_list[high], ship_list[i]
            pivot_index = i
            if pivot_index - low < high - pivot_index:
                optimized_quicksort(ship_list, low, pivot_index - 1)
                low = pivot_index + 1
            else:
                optimized_quicksort(ship_list, pivot_index + 1, high)
                high = pivot_index - 1
        else:
            for i in range(low, high):
                min_idx = i
                for j in range(i + 1, high + 1):
                    if ship_list[j] < ship_list[min_idx]:
                        min_idx = j
                if min_idx != i:
                    ship_list[i], ship_list[min_idx] = ship_list[min_idx], ship_list[i]
            break

def measure_time(func, ship_list):
    start_time = time.time()
    func(ship_list, 0, len(ship_list) - 1)
    end_time = time.time()
    return end_time - start_time

def benchmark_sorting_algorithm(sort_function, ship_list_sizes):
    times = []
    for size in tqdm(ship_list_sizes):
        ship_list = [Ship(random.randint(10, 100)) for _ in range(size)]
        time_taken = measure_time(sort_function, ship_list)
        times.append(time_taken)
    return times

def plot_results(ship_list_sizes, times, algorithm_name, scaling_factor):
    plt.figure()
    plt.plot(ship_list_sizes, times, label="Measured Time")
    
    theoretical_times = []
    base_size = ship_list_sizes[0]
    base_time = times[0]
    
    for size in ship_list_sizes:
        ratio = (size / base_size) ** 2
        time = base_time * ratio * scaling_factor
        theoretical_times.append(time)
    
    plt.plot(ship_list_sizes, theoretical_times, label="O(n^2)")
    
    plt.title(f"{algorithm_name} Benchmark")
    plt.xlabel("Ship List Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig(f"images/{algorithm_name.lower().replace(' ', '_')}_benchmark.png")
if __name__ == "__main__":
    ship_list_sizes = [i*2 for i in range(1, 200)]
    scaling_factors = [0.01, 0.05, 0.03, 1, 0.0000005, 0.02]  # Adjusted scaling factors

    algorithms = {
        "Standard Quicksort": quicksort_standard,
        "Improved Pivot Quicksort": quicksort_improved_pivot,
        "Random Pivot Quicksort": quicksort_random_pivot,
        "Three-way Quicksort": quicksort_three_way,
        "Introsort": introsort,
        "Optimized Quicksort": optimized_quicksort
    }

    for algorithm_name, sort_function in algorithms.items():
        times = benchmark_sorting_algorithm(sort_function, ship_list_sizes)
        plot_results(ship_list_sizes, times, algorithm_name, scaling_factors[len(algorithms)-1])
