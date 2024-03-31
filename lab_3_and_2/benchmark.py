from utils import benchmark
import matplotlib.pyplot as plt
from config import Config
import numpy as np

def moving_average(data, window_size):
    """Calculate moving average of data."""
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def run_benchmark(operations=[]):
    data = benchmark(operations)
    operations = {}
    for entry in data:
        operation = entry['operation']
        if operation not in operations:
            operations[operation] = {'sizes': [], 'times': []}
        operations[operation]['sizes'].append(entry['size'])
        operations[operation]['times'].append(entry['time'])

    plt.figure(figsize=(10, 6))
    for operation, values in operations.items():
        # Calculate moving average for time data
        smoothed_times = moving_average(values['times'], window_size=3)
        plt.plot(values['sizes'][:len(smoothed_times)], smoothed_times, label=operation)

    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title('Performance of Operations by Graph Size (Smoothed)')
    plt.legend()
    plt.grid(True)
    plt.savefig(Config.output_dir + 'benchmark_smoothed.png')
    plt.show()


if __name__ == "__main__":
    run_benchmark()
