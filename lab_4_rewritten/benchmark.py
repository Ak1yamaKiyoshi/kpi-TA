
import matplotlib.pyplot as plt
from main import SingleLinkedList
import timeit
from tqdm import tqdm
import seaborn as sns
import numpy as np
import os

def moving_average(data, window_size):
    weights = np.repeat(1.0, window_size) / window_size
    return np.convolve(data, weights, 'valid')

def benchmark_linked_list(max_size, smoothing_window=10):
    append_times = []
    remove_head_times = []
    sizes = []

    for size in tqdm(range(1, max_size + 1)):
        linked_list = SingleLinkedList()
        for _ in range(size):
            linked_list.append(None)

        setup_code = """
from main import SingleLinkedList
linked_list = SingleLinkedList()
for _ in range({}):
    linked_list.append(None)
""".format(size)

        append_stmt = "linked_list.append(None)"
        append_time = timeit.timeit(stmt=append_stmt, setup=setup_code, number=100)
        append_times.append(append_time)

        remove_head_stmt = "linked_list.remove_head()"
        remove_head_time = timeit.timeit(stmt=remove_head_stmt, setup=setup_code, number=1000)
        remove_head_times.append(remove_head_time)

        sizes.append(size)

    append_times_smoothed = moving_average(append_times, smoothing_window)
    remove_head_times_smoothed = moving_average(remove_head_times, smoothing_window)

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes[:-smoothing_window+1], append_times_smoothed, label="append (Smoothed)", color='blue')
    plt.plot(sizes[:-smoothing_window+1], remove_head_times_smoothed, label="remove_head (Smoothed)", color='blue', linestyle='--')

    plt.xlabel("List Size")
    if not os.path.exists("outputs"):
        os.mkdir('outputs')
    plt.savefig(os.path.join('outputs', 'benchmark.png'))
    plt.ylabel("Time (seconds)")
    plt.title("Linked List Performance Benchmark")
    plt.legend()
    plt.show()

benchmark_linked_list(1000)
