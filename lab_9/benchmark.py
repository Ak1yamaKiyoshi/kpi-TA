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
        for j in range(0, n - i - 1):
            if ship_list[j].num_matroses > ship_list[j + 1].num_matroses:
                ship_list[j], ship_list[j + 1] = ship_list[j + 1], ship_list[j]


def counting_sort(ship_list):
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


# Benchmarking function for Bubble Sort
def benchmark_bubble_sort(ship_list_sizes):
    bubble_sort_times = []
    for size in tqdm(ship_list_sizes):
        ship_list = [Ship(random.randint(10, 100)) for _ in range(size)]
        bubble_sort_time = measure_time(bubble_sort, ship_list)
        bubble_sort_times.append(bubble_sort_time)
    return bubble_sort_times


# Benchmarking function for Shell Sort
def benchmark_shell_sort(ship_list_sizes):
    shell_sort_times = []
    for size in tqdm(ship_list_sizes):
        ship_list = [Ship(random.randint(10, 100)) for _ in range(size)]
        shell_sort_time = measure_time(shell_sort, ship_list)
        shell_sort_times.append(shell_sort_time)
    return shell_sort_times


# Benchmarking function for Counting Sort
def benchmark_counting_sort(ship_list_sizes):
    counting_sort_times = []
    for size in tqdm(ship_list_sizes):
        ship_list = [Ship(random.randint(10, 100)) for _ in range(size)]
        counting_sort_time = measure_time(counting_sort, ship_list)
        counting_sort_times.append(counting_sort_time)
    return counting_sort_times


# Function to plot benchmarking results
def plot_results(ship_list_sizes, times, title, filename, scaling_factor):
    plt.figure()
    plt.plot(ship_list_sizes, times, label="Measured Time")
    
    theoretical_times = []
    base_size = ship_list_sizes[0]
    base_time = times[0]  # Base time from measured data
    
    for size in ship_list_sizes:
        ratio = (size / base_size) ** 2
        time = base_time * ratio * scaling_factor
        theoretical_times.append(time)
    
    plt.plot(ship_list_sizes, theoretical_times, label="O(n^2)")
    
    plt.title(title)
    plt.xlabel("Ship List Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("images/"+filename)

if __name__ == "__main__":
    ship_list_sizes = [i for i in range (1, 600)]  # Adjust the list sizes as needed
    scaling_factors = [0.05, 0.0045, 0.00003]  # Adjust scaling factors for each algorithm

    # Benchmarking Bubble Sort
    bubble_sort_times = benchmark_bubble_sort(ship_list_sizes)
    plot_results(ship_list_sizes, bubble_sort_times, "Bubble Sort Benchmark", "bubble_sort_benchmark.png", scaling_factors[0])

    # Benchmarking Shell Sort
    shell_sort_times = benchmark_shell_sort(ship_list_sizes)
    plot_results(ship_list_sizes, shell_sort_times, "Shell Sort Benchmark", "shell_sort_benchmark.png", scaling_factors[1])

    # Benchmarking Counting Sort
    counting_sort_times = benchmark_counting_sort(ship_list_sizes)
    plot_results(ship_list_sizes, counting_sort_times, "Counting Sort Benchmark", "counting_sort_benchmark.png", scaling_factors[2])
