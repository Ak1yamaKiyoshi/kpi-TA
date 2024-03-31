
import matplotlib.pyplot as plt
from main import SingleLinkedList, SingleLinkedListArray
import timeit
from tqdm import tqdm
import seaborn as sns
import numpy as np
import os

def moving_average(data, window_size):
    weights = np.repeat(1.0, window_size) / window_size
    return np.convolve(data, weights, 'valid')

def benchmark_linked_list(max_size, smoothing_window=2):
    append_times_linked_list = []
    remove_head_times_linked_list = []
    append_times_array = []
    remove_head_times_array = []
    sizes = []

    for size in tqdm(range(1, max_size + 1)):
        linked_list = SingleLinkedList()
        array_list = SingleLinkedListArray()

        # Benchmark for SingleLinkedList
        setup_code_linked_list = """
from main import SingleLinkedList
linked_list = SingleLinkedList()
for _ in range({}):
    linked_list.append(None)
""".format(size)

        append_stmt_linked_list = "linked_list.append(None)"
        append_time_linked_list = timeit.timeit(stmt=append_stmt_linked_list, setup=setup_code_linked_list, number=1000)
        append_times_linked_list.append(append_time_linked_list)

        remove_head_stmt_linked_list = "linked_list.remove_head()"
        remove_head_time_linked_list = timeit.timeit(stmt=remove_head_stmt_linked_list, setup=setup_code_linked_list, number=1000)
        remove_head_times_linked_list.append(remove_head_time_linked_list)

        # Benchmark for SingleLinkedListArray
        setup_code_array = """
from main import SingleLinkedListArray
array_list = SingleLinkedListArray()
for _ in range({}):
    array_list.append(None)
""".format(size)

        append_stmt_array = "array_list.append(None)"
        append_time_array = timeit.timeit(stmt=append_stmt_array, setup=setup_code_array, number=1000)
        append_times_array.append(append_time_array)

        remove_head_stmt_array = "array_list.remove_head()"
        remove_head_time_array = timeit.timeit(stmt=remove_head_stmt_array, setup=setup_code_array, number=1000)
        remove_head_times_array.append(remove_head_time_array)

        sizes.append(size)

    append_times_linked_list_smoothed = moving_average(append_times_linked_list, smoothing_window)
    remove_head_times_linked_list_smoothed = moving_average(remove_head_times_linked_list, smoothing_window)
    append_times_array_smoothed = moving_average(append_times_array, smoothing_window)
    remove_head_times_array_smoothed = moving_average(remove_head_times_array, smoothing_window)

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    plt.plot(sizes[:-smoothing_window+1], append_times_linked_list_smoothed, label="append (Linked List)", color='blue', alpha=0.4)
    plt.plot(sizes[:-smoothing_window+1], remove_head_times_linked_list_smoothed, label="remove_head (Linked List)", color='blue', linestyle='--', alpha=0.6)

    plt.plot(sizes[:-smoothing_window+1], append_times_array_smoothed, label="append (Array)", color='red', alpha=0.4)
    plt.plot(sizes[:-smoothing_window+1], remove_head_times_array_smoothed, label="remove_head (Array)", color='red', linestyle='--', alpha=0.4)

    plt.xlabel("List Size")
    if not os.path.exists("outputs"):
        os.mkdir('outputs')
    plt.savefig(os.path.join('outputs', 'benchmark.png'))
    plt.ylabel("Time (seconds)")
    plt.title("Linked List Performance Benchmark")
    plt.legend()
    plt.show()

benchmark_linked_list(1000)
