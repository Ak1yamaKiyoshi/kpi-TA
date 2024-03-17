from utils import benchmark
import matplotlib.pyplot as plt
from config import Config


def run_benchmark():
    data = benchmark()
    operations = {}
    for entry in data:
        operation = entry['operation']
        if operation not in operations:
            operations[operation] = {'sizes': [], 'times': []}
        operations[operation]['sizes'].append(entry['size'])
        operations[operation]['times'].append(entry['time'])

    plt.figure(figsize=(10, 6))
    for operation, values in operations.items():
        plt.plot(values['sizes'], values['times'], label=operation)

    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.title('Performance of Operations by Graph Size')
    plt.legend()
    plt.grid(True)
    plt.savefig(Config.output_dir + 'benchmark.png')
    plt.show()

if __name__ == "__main__":
    run_benchmark()
