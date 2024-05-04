import time
import matplotlib.pyplot as plt
from main import RedBlackTree

def measure_time(func, tree, *args):
    start_time = time.time()
    result = func(tree, *args)
    end_time = time.time()
    return end_time - start_time

def benchmark_insert(tree_sizes):
    insert_times = []
    for n in tree_sizes:
        tree = RedBlackTree()
        for i in range(min(n, 990)):  # Limit tree size to 990
            tree.insert(i)
        insert_time = measure_time(RedBlackTree.insert, tree, min(n, 990))
        insert_times.append(insert_time)
    return insert_times

def plot_results(tree_sizes, times, title, filename):
    
    theoretical_times = []
    base_size = tree_sizes[0]
    base_time = times[0]
    scaling_factor = 0.000006 

    for size, time in zip(tree_sizes, times):
        ratio = (size / base_size) ** 2
        theoretical_time =  base_time * ratio * scaling_factor
        theoretical_times.append(theoretical_time)
    
    plt.figure()
    plt.plot(tree_sizes, times, label="Measured Time")
    plt.plot(tree_sizes, theoretical_times, label="O(n)^2")
    plt.title(title)
    plt.xlabel("Tree Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.savefig("./images/"+ filename)  

if __name__ == "__main__":
    tree_sizes = [10, 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

    insert_times = benchmark_insert(tree_sizes)
    plot_results(tree_sizes, insert_times, "Red-Black Tree Insertion Benchmark", "red_black_tree_insertion_benchmark.png")

    