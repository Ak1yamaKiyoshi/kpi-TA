import time
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

import time
import random
import tkinter as tk
from tkinter import ttk, simpledialog
import matplotlib.pyplot as plt




# Клас Сортувань
class Sortings:
    @staticmethod
    def merge_sort(arr, viz_steps=None):
        if viz_steps is None:
            viz_steps = []

        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            Sortings.merge_sort(left, viz_steps)
            Sortings.merge_sort(right, viz_steps)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    viz_steps.append(('c', k, i, left[i], right[j]))  # Додано порівняння
                    i += 1
                else:
                    arr[k] = right[j]
                    viz_steps.append(('c', k, len(left) + j, left[i], right[j]))  # Додано порівняння
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                viz_steps.append(('mv', k, i, left[i], None))  # Додано переміщення
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                viz_steps.append(('mv', k, len(left) + j, right[j], None))  # Додано переміщення
                j += 1
                k += 1

        return viz_steps

    @staticmethod
    def smooth_sort(arr, viz_steps=None):
        if viz_steps is None:
            viz_steps = []

        def sift_down(start, end):
            root = start
            while True:
                child = root * 2 + 1
                if child > end:
                    break
                if child + 1 <= end and arr[child] < arr[child + 1]:
                    child += 1
                if arr[root] < arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    viz_steps.append(('s', root, child))
                    root = child
                else:
                    break

        for i in range((len(arr) - 1) // 2, -1, -1):
            sift_down(i, len(arr) - 1)

        for i in range(len(arr) - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            viz_steps.append(('s', 0, i))
            sift_down(0, i - 1)

        return viz_steps

    @staticmethod
    def quick_sort(arr, viz_steps=None):
        if viz_steps is None:
            viz_steps = []

        def partition(low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    viz_steps.append(('s', i, j))
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            viz_steps.append(('s', i + 1, high))
            return i + 1

        def quicksort(low, high):
            if low < high:
                pi = partition(low, high)
                quicksort(low, pi - 1)
                quicksort(pi + 1, high)

        quicksort(0, len(arr) - 1)
        return viz_steps

# Клас програми
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorting Visualizer")
        self.geometry("500x300")
        self.create_widgets()
        self.arr = []
        self.viz_steps = []
        self.sorting_method = None
        self.custom_theme()


    def create_widgets(self):
        # Left frame for sort method, buttons, and message text
        left_frame = tk.Frame(self)
        left_frame.pack(side="left", padx=10, pady=10)

        # Buttons in left frame
        button_width = 15
        button_height = 2

        # Sort method dropdown in left frame
        self.sort_method_var = tk.StringVar()
        self.sort_method_menu = ttk.Combobox(left_frame, width=button_width, height=button_height, textvariable=self.sort_method_var, values=["Merge Sort", "Smooth Sort", "Quick Sort"])
        self.sort_method_menu.pack(side="top", padx=10, pady=5)
        self.sort_method_var.set("Merge Sort")

        self.add_button = tk.Button(left_frame, text="Add Number", command=self.add_number, width=button_width, height=button_height)
        self.add_button.pack(side="top", padx=10, pady=5)

        self.remove_button = tk.Button(left_frame, text="Remove Number", command=self.remove_number, width=button_width, height=button_height)
        self.remove_button.pack(side="top", padx=10, pady=5)

        self.shuffle_button = tk.Button(left_frame, text="Shuffle", command=self.shuffle_array, width=button_width, height=button_height)
        self.shuffle_button.pack(side="top", padx=10, pady=5)

        self.sort_button = tk.Button(left_frame, text="Sort", command=self.sort_array, width=button_width, height=button_height)
        self.sort_button.pack(side="top", padx=10, pady=5)

        # Message text in left frame
        self.message_text = tk.Text(left_frame, height=5, width=30)
        self.message_text.pack(side="bottom", padx=10, pady=10)

        # Right frame for array display and visualization text
        right_frame = tk.Frame(self)
        right_frame.pack(side="right", padx=10, pady=10)

        # Array display in right frame
        self.arr_label = tk.Label(right_frame, text="Array: []")
        self.arr_label.pack(side="top", padx=10, pady=10)

        # Visualization text in right frame
        viz_text_width = 50
        viz_text_height = 20
        self.viz_text = tk.Text(right_frame, height=viz_text_height, width=viz_text_width)
        self.viz_text.pack(side="bottom", padx=10, pady=10)

    def custom_theme(self):
        style = ttk.Style()
        style.theme_create("Custom", parent="alt", settings={
            "TCombobox": {"configure": {"fieldbackground": "light blue"}},
            "TButton": {"configure": {"background": "light green", "font": ("Helvetica", 12)}},
            "TLabel": {"configure": {"foreground": "dark blue", "font": ("Helvetica", 14, "bold")}},
            "Text": {"configure": {"background": "light yellow", "foreground": "dark green", "font": ("Courier", 10)}}
        })
        style.theme_use("Custom")


    def add_number(self):
        num = simpledialog.askinteger("Add Number", "Enter a number to add to the array")
        if num is not None:
            self.arr.append(num)
            self.update_array_label()

    def remove_number(self):
        if self.arr:
            num = simpledialog.askinteger("Remove Number", "Enter the index of the number to remove")
            if num is not None and 0 <= num < len(self.arr):
                self.arr.pop(num)
                self.update_array_label()

    @staticmethod
    def insert_newlines(string, every=64):
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i+every])
        return '\n'.join(lines)

    def custom_print(self, array, end=5):
        string = "["
        for i, element in enumerate(array):
            if i % end == 0:
                string += "\n"
            string += f"{element:03} "
        string += "]"
        return string


    def update_array_label(self):
        self.arr_label.config(text=f"Array: {self.custom_print(self.arr, 7)}")


    def shuffle_array(self):
        random.shuffle(self.arr)
        self.update_array_label()

    def sort_array(self):
        self.viz_text.delete('1.0', tk.END)
        self.message_text.delete('1.0', tk.END)
        self.sorting_method = self.sort_method_var.get()
        start_time = time.time()
        if self.sorting_method == "Merge Sort":
            self.viz_steps = Sortings.merge_sort(self.arr)
        elif self.sorting_method == "Smooth Sort":
            self.viz_steps = Sortings.smooth_sort(self.arr)
        elif self.sorting_method == "Quick Sort":
            self.viz_steps = Sortings.quick_sort(self.arr)
        end_time = time.time()
        self.visualize_sorting()
        self.display_sorting_info(end_time - start_time)
        self.update_array_label()

    def visualize_sorting(self):
        for step in self.viz_steps:
            try:
                operation, idx1, idx2, val1, val2, *args = step
            except:
                operation, idx1, idx2 = step

            if operation == 'c':
                self.viz_text.insert(tk.END, f"Compared {val1} and {val2}\n")
            elif operation == 's':
                self.viz_text.insert(tk.END, f"Swapped {self.arr[idx1]} and {self.arr[idx2]}\n")
            elif operation == 'mv':
                self.viz_text.insert(tk.END, f"Moved {val1} to index {idx1}\n")
            self.update_array_label()
            self.update()

    def display_sorting_info(self, elapsed_time):
        num_comparisons = sum(1 for step in self.viz_steps if step[0] == 'c')
        num_swaps = sum(1 for step in self.viz_steps if step[0] == 'mv')
        message = f"Sorting Method: {self.sorting_method}\n"
        message += f"Time Elapsed: {elapsed_time:.6f} seconds\n"
        message += f"Number of Comparisons: {num_comparisons}\n"
        message += f"Number of Swaps: {num_swaps}"
        self.message_text.insert(tk.END, message)

# Клас тестувань
import random
import time
import matplotlib.pyplot as plt

class TestingSorts:
    def __init__(self):
        self.array_lengths = [i*4 for i in range(500)]
        self.merge_sort_times = []
        self.smooth_sort_times = []
        self.quick_sort_times = []
        self.merge_sort_times_random = []
        self.smooth_sort_times_random = []
        self.quick_sort_times_random = []
        self.merge_sort_times_partially_sorted = []
        self.smooth_sort_times_partially_sorted = []
        self.quick_sort_times_partially_sorted = []
        self.merge_sort_times_repeated = []
        self.smooth_sort_times_repeated = []
        self.quick_sort_times_repeated = []

    def test_sorting(self):
        for length in self.array_lengths:
            arr = [random.randint(0, 1000000) for _ in range(length)]
            arr_random = arr.copy()
            arr_partially_sorted = sorted(arr_random[:length // 2]) + arr_random[length // 2:]
            arr_repeated = [random.randint(0, 100) for _ in range(length // 10)] * 10

            # Merge Sort
            start_time = time.time()
            Sortings.merge_sort(arr.copy())
            end_time = time.time()
            self.merge_sort_times.append(end_time - start_time)

            start_time = time.time()
            Sortings.merge_sort(arr_random.copy())
            end_time = time.time()
            self.merge_sort_times_random.append(end_time - start_time)

            start_time = time.time()
            Sortings.merge_sort(arr_partially_sorted.copy())
            end_time = time.time()
            self.merge_sort_times_partially_sorted.append(end_time - start_time)

            start_time = time.time()
            Sortings.merge_sort(arr_repeated.copy())
            end_time = time.time()
            self.merge_sort_times_repeated.append(end_time - start_time)

            # Smooth Sort
            start_time = time.time()
            Sortings.smooth_sort(arr.copy())
            end_time = time.time()
            self.smooth_sort_times.append(end_time - start_time)

            start_time = time.time()
            Sortings.smooth_sort(arr_random.copy())
            end_time = time.time()
            self.smooth_sort_times_random.append(end_time - start_time)

            start_time = time.time()
            Sortings.smooth_sort(arr_partially_sorted.copy())
            end_time = time.time()
            self.smooth_sort_times_partially_sorted.append(end_time - start_time)

            start_time = time.time()
            Sortings.smooth_sort(arr_repeated.copy())
            end_time = time.time()
            self.smooth_sort_times_repeated.append(end_time - start_time)

            # Quick Sort
            start_time = time.time()
            Sortings.quick_sort(arr.copy())
            end_time = time.time()
            self.quick_sort_times.append(end_time - start_time)

            start_time = time.time()
            Sortings.quick_sort(arr_random.copy())
            end_time = time.time()
            self.quick_sort_times_random.append(end_time - start_time)

            start_time = time.time()
            Sortings.quick_sort(arr_partially_sorted.copy())
            end_time = time.time()
            self.quick_sort_times_partially_sorted.append(end_time - start_time)

            start_time = time.time()
            Sortings.quick_sort(arr_repeated.copy())
            end_time = time.time()
            self.quick_sort_times_repeated.append(end_time - start_time)

    def plot_results(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.array_lengths, self.merge_sort_times, label="Merge Sort")
        plt.plot(self.array_lengths, self.smooth_sort_times, label="Smooth Sort")
        plt.plot(self.array_lengths, self.quick_sort_times, label="Quick Sort")
        plt.plot(self.array_lengths, self.merge_sort_times_random, label="Merge Sort (Random)")
        plt.plot(self.array_lengths, self.smooth_sort_times_random, label="Smooth Sort (Random)")
        plt.plot(self.array_lengths, self.quick_sort_times_random, label="Quick Sort (Random)")
        plt.plot(self.array_lengths, self.merge_sort_times_partially_sorted, label="Merge Sort (Partially Sorted)")
        plt.plot(self.array_lengths, self.smooth_sort_times_partially_sorted, label="Smooth Sort (Partially Sorted)")
        plt.plot(self.array_lengths, self.quick_sort_times_partially_sorted, label="Quick Sort (Partially Sorted)")
        plt.plot(self.array_lengths, self.merge_sort_times_repeated, label="Merge Sort (Repeated)")
        plt.plot(self.array_lengths, self.smooth_sort_times_repeated, label="Smooth Sort (Repeated)")
        plt.plot(self.array_lengths, self.quick_sort_times_repeated, label="Quick Sort (Repeated)")
        plt.xlabel("Array Length")
        plt.ylabel("Time (seconds)")
        plt.title("Sorting Algorithm Performance")
        plt.legend()
        plt.show()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    test = TestingSorts()
    test.test_sorting()
    test.plot_results()