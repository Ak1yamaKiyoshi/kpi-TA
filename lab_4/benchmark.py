import timeit
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import random
from single_linked_list import SingleLinkedList

def benchmark_append(size):
    setup_code = f"""
from single_linked_list import SingleLinkedList
import random
sll = SingleLinkedList()
"""
    stmt = "sll.append(random.randint(0, 100))"
    return timeit.timeit(stmt, setup=setup_code, number=size)

def benchmark_prepend(size):
    setup_code = f"""
from single_linked_list import SingleLinkedList
import random
sll = SingleLinkedList()
"""
    stmt = "sll.prepend(random.randint(0, 100))"
    return timeit.timeit(stmt, setup=setup_code, number=size)

def benchmark_delete(size):
    setup_code = f"""
from single_linked_list import SingleLinkedList
import random
sll = SingleLinkedList()
for i in range({size}):
    sll.append(i)
"""
    stmt = "sll.delete(random.randint(0, 100))"
    return timeit.timeit(stmt, setup=setup_code, number=size)

def benchmark_find(size):
    setup_code = f"""
from single_linked_list import SingleLinkedList
import random
sll = SingleLinkedList()
for i in range({size}):
    sll.append(i)
"""
    stmt = "sll.find(random.randint(0, 100))"
    return timeit.timeit(stmt, setup=setup_code, number=size)

def benchmark_index_of(size):
    setup_code = f"""
from single_linked_list import SingleLinkedList
import random
sll = SingleLinkedList()
for i in range({size}):
    sll.append(i)
"""
    stmt = "sll.index_of(lambda x: x.value == random.randint(0, 100))"
    return timeit.timeit(stmt, setup=setup_code, number=size)

def benchmark_operations():
    sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    operations = [benchmark_append, benchmark_prepend, benchmark_delete, benchmark_find, benchmark_index_of]
    results = {op.__name__: [] for op in operations}

    for size in tqdm(sizes, desc="Sizes"):
        mean_list_size = size  # Assuming mean list size is equal to the current size
        for operation in tqdm(operations, desc="Operations", leave=False):
            result = operation(mean_list_size)
            results[operation.__name__].append(result)

    return sizes, results


def plot_results(sizes, results):
    for operation, timings in results.items():
        plt.plot(sizes, timings, label=operation)
        plt.savefig(os.path.join('outputs', f'{operation}_benchmark.png'))
        plt.show()

    for operation, timings in results.items():
        plt.plot(sizes, timings, label=operation)

    plt.xlabel('Size of List')
    plt.ylabel('Time (seconds)')
    plt.title('Benchmarking Single Linked List Operations')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join('outputs', 'benchmark.png'))
    plt.show()

if __name__ == "__main__":
    os.makedirs('outputs', exist_ok=True)
    sizes, results = benchmark_operations()
    plot_results(sizes, results)
