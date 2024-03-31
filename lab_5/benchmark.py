import timeit
import matplotlib.pyplot as plt
from program import HashTableApp

def benchmark_division(table_size, key, iterations):
    setup_code = f"""
from __main__ import HashTableApp
app = HashTableApp()
app.table_size = {table_size}
    """
    division_code = f"""
for _ in range({iterations}):
    app.hash_division({key}, 0, {table_size})
    """
    return timeit.timeit(division_code, setup=setup_code, number=1)

def benchmark_multiplication(table_size, key, iterations):
    setup_code = f"""
from __main__ import HashTableApp
app = HashTableApp()
app.table_size = {table_size}
    """
    multiplication_code = f"""
for _ in range({iterations}):
    app.hash_multiplication({key}, 0, {table_size})
    """
    return timeit.timeit(multiplication_code, setup=setup_code, number=1)

def benchmark_list(iterations):
    list_creation_code = f"""
my_list = list(range({iterations}))
    """
    return timeit.timeit(f'random_index = my_list.index({iterations}//2)', setup=list_creation_code, number=1)

if __name__ == "__main__":
    table_sizes = [5*10000, 25*10000, 100*10000, 250*10000, 1000*10000]
    key = 123456789  
    iterations = 100000
    division_times = []
    multiplication_times = []
    list_times = []

    for size in table_sizes:
        division_time = benchmark_division(size, key, iterations)
        multiplication_time = benchmark_multiplication(size, key, iterations)
        list_time = benchmark_list(iterations)

        division_times.append(division_time)
        multiplication_times.append(multiplication_time)
        list_times.append(list_time)

    plt.plot(table_sizes, division_times, label='Division Hashing')
    plt.plot(table_sizes, multiplication_times, label='Multiplication Hashing')
    plt.plot(table_sizes, list_times, label='List')
    plt.xlabel('Table Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Hashing vs List Benchmark for Different Table Sizes')
    plt.legend()
    plt.show()
