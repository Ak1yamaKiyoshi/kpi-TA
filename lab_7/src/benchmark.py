from src.bst import BinarySearchTree

import time
import random
import matplotlib.pyplot as plt
from src.node import Node
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np


# Function to generate random BSTs
def generate_bst(size, balanced=False):
    tree = BinarySearchTree()
    values = list(range(size))
    if balanced:
        values.sort()
    else:
        random.shuffle(values)
    for value in values:
        tree.insert(value)
    return tree

# Timing functions for each operation
def time_removal(tree, value):
    start_time = time.time()
    tree.remove(value)
    end_time = time.time()
    return end_time - start_time

def time_insertion(tree, value):
    start_time = time.time()
    tree.insert(value)
    end_time = time.time()
    return end_time - start_time

def time_traversal(tree, traversal_type):
    start_time = time.time()
    if traversal_type == 'pre_order':
        tree.pre_order_to_array()
    elif traversal_type == 'in_order':
        tree.in_order_to_array()
    else:
        tree.post_order_to_array()
    end_time = time.time()
    return end_time - start_time

def time_binary_search(tree, value):
    start_time = time.time()
    tree.binarySearch(value)
    end_time = time.time()
    return end_time - start_time

def main():
    test_cases = [ 
        {'name': 'Empty Tree',             'size': 0, 'balanced': False, 'values': []},
        {'name': 'Single Node Tree',       'size': 1, 'balanced': False, 'values': [0]},
        {'name': 'Small Balanced Tree',    'size': 10, 'balanced': True, 'values': list(range(10))},
        {'name': 'Small Unbalanced Tree',  'size': 10, 'balanced': False, 'values': list(range(10))},
        {'name': 'Medium Balanced Tree',   'size': 100, 'balanced': True, 'values': list(range(100))},
        {'name': 'Medium Unbalanced Tree', 'size': 100, 'balanced': False, 'values': list(range(100))},
        {'name': 'Large Balanced Tree',    'size': 1000, 'balanced': True, 'values': list(range(1000))},
        {'name': 'Large Unbalanced Tree',  'size': 1000, 'balanced': False, 'values': list(range(1000))}
    ]

    results = {}
    for test_case in test_cases:
        tree = generate_bst(test_case['size'], test_case['balanced'])
        results[test_case['name']] = {
            'removal': [],
            'insertion': [],
            'binary_search': [],
            'failed_binary_search': []  # Add benchmark for failed binary search
        }

        for value in test_case['values']:
            time_taken = time_removal(tree, value)
            results[test_case['name']]['removal'].append(time_taken)

        for value in test_case['values']:
            time_taken = time_insertion(tree, value)
            results[test_case['name']]['insertion'].append(time_taken)

        for value in test_case['values']:
            time_taken = time_binary_search(tree, value)
            results[test_case['name']]['binary_search'].append(time_taken)

        for value in test_case['values']:
            time_taken = time_binary_search(tree,10000)  # A value guaranteed not to be in the tree
            results[test_case['name']]['failed_binary_search'].append(time_taken)

    for operation in ['removal', 'insertion', 'binary_search', 'failed_binary_search']:  # Include failed binary search in plotting
        plt.figure(figsize=(18, 6))
        for test_case in test_cases:
                
            try:
                window_length = min(11, len(test_case['values']))
                smoothed_data = np.convolve(results[test_case['name']][operation], np.ones(window_length)/window_length, mode='valid')
                plt.plot(test_case['values'][:len(smoothed_data)], smoothed_data, label=test_case['name'])
            except:
                plt.plot(test_case['values'], results[test_case['name']][operation], label=test_case['name'], alpha=0.9)
                
        plt.title(f'Performance of {operation} operation')
        plt.xlabel('Input Size')
        plt.ylabel('Execution Time')
        plt.legend()
        plt.savefig(f"images/{operation}")
        plt.show()
