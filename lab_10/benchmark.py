import time
import random
import matplotlib.pyplot as plt

from main import ShipSortGUI, Ship

def generate_reversed_array(n):
    ships = [Ship(i) for i in range(n, 0, -1)]
    return ships

def generate_half_sorted_array(n):
    half = n // 2
    sorted_half = [Ship(i) for i in range(half)]
    unsorted_half = [Ship(random.randint(10, 100)) for _ in range(n - half)]
    ships = sorted_half + unsorted_half
    random.shuffle(ships)
    return ships

def generate_mostly_sorted_array(n, sorted_ratio=0.8):
    sorted_count = int(n * sorted_ratio)
    sorted_ships = [Ship(i) for i in range(sorted_count)]
    unsorted_ships = [Ship(random.randint(10, 100)) for _ in range(n - sorted_count)]
    ships = sorted_ships + unsorted_ships
    random.shuffle(ships)
    return ships

def generate_all_same_array(n, value=50):
    ships = [Ship(value) for _ in range(n)]
    return ships

def run_benchmark(array_sizes, test_cases):
    sorting_algorithms = ["Stable Quicksort", "Improved Pivot Quicksort", "Random Pivot Quicksort",
                          "Three-way Quicksort", "Introsort", "Optimized Quicksort"]

    results = {}
    for sorting_alg in sorting_algorithms:
        results[sorting_alg] = {}
        for test_case in test_cases:
            results[sorting_alg][test_case] = []

    for size in array_sizes:
        print(f"Running benchmark for array size: {size}")
        for test_case, generator in test_cases.items():
            ships = generator(size)
            for sorting_alg in sorting_algorithms:
                app = ShipSortGUI()
                app.ship_list = ships
                start_time = time.time()
                app.sort_ships()
                end_time = time.time()
                elapsed_time = end_time - start_time
                results[sorting_alg][test_case].append(elapsed_time)

    return results

def plot_results(results, array_sizes):
    for sorting_alg, alg_results in results.items():
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        axs = axs.flatten()

        for i, test_case in enumerate(["Reversed Array", "Half Sorted Array", "80% Sorted Array", "All Same"]):
            times = alg_results[test_case]
            axs[i].plot(array_sizes, times)
            axs[i].set_title(f"{test_case} - {sorting_alg}")
            axs[i].set_xlabel("Array Size")
            axs[i].set_ylabel("Time (s)")

        fig.tight_layout()
        plt.savefig(f"{sorting_alg}_benchmark.png")

if __name__ == "__main__":
    array_sizes = [i * 5 for i in range(50)]
    test_cases = {
        "Reversed Array": generate_reversed_array,
        "Half Sorted Array": generate_half_sorted_array,
        "80% Sorted Array": lambda n: generate_mostly_sorted_array(n, 0.8),
        "All Same": generate_all_same_array
    }

    results = run_benchmark(array_sizes, test_cases)
    plot_results(results, array_sizes)