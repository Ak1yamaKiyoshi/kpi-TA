import tkinter as tk
import random


class Ship:
    def __init__(self, num_matroses):
        self.num_matroses = num_matroses

    def __str__(self):
        return f"Ship with {self.num_matroses} matroses"
    
    def __lt__(self, other):
        return self.num_matroses < other.num_matroses
    
    def __le__(self, other):
        return self.num_matroses <= other.num_matroses
    
    def __eq__(self, other):
        return self.num_matroses == other.num_matroses
    
    def __ne__(self, other):
        return self.num_matroses != other.num_matroses
    
    def __gt__(self, other):
        return self.num_matroses > other.num_matroses
    
    def __ge__(self, other):
        return self.num_matroses >= other.num_matroses


class ShipSortGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ship Sorting GUI")
        
        self.ship_list = []
        self.movements = []
        
        self.ship_listbox = tk.Listbox(self, width=50, height=20)
        self.ship_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.movements_text = tk.Text(self, width=50, height=20)
        self.movements_text.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.sort_alg_var = tk.StringVar()
        self.sort_alg_var.set("Stable Quicksort")  # Default to Stable Quicksort
        
        self.sort_menu = tk.OptionMenu(self, self.sort_alg_var, "Stable Quicksort", "Improved Pivot Quicksort", "Random Pivot Quicksort", "Three-way Quicksort", "Introsort", "Optimized Quicksort")
        self.sort_menu.pack(side=tk.TOP, padx=10, pady=10)
        
        self.shuffle_button = tk.Button(self, text="Shuffle", command=self.shuffle_ships)
        self.shuffle_button.pack(side=tk.TOP, padx=10, pady=10)
        
        self.sort_button = tk.Button(self, text="Sort", command=self.sort_ships)
        self.sort_button.pack(side=tk.TOP, padx=10, pady=10)
        
        self.add_ship_button = tk.Button(self, text="Add Ship", command=self.add_ship)
        self.add_ship_button.pack(side=tk.TOP, padx=10, pady=10)
        

    def add_ship(self):
        num_matroses = random.randint(10, 100)  # Random number of matroses for demonstration
        ship = Ship(num_matroses)
        self.ship_list.append(ship)
        self.ship_listbox.insert(tk.END, str(ship))
        
    def shuffle_ships(self):
        random.shuffle(self.ship_list)
        self.update_ship_listbox()
        
    def update_ship_listbox(self):
        self.ship_listbox.delete(0, tk.END)
        for ship in self.ship_list:
            self.ship_listbox.insert(tk.END, str(ship))
        
    def sort_ships(self):
        self.movements = []  
        self.update_ship_listbox()
        sort_alg = self.sort_alg_var.get()
        if sort_alg == "Stable Quicksort":
            self.stable_quicksort(0, len(self.ship_list) - 1)
        elif sort_alg == "Improved Pivot Quicksort":
            self.improved_pivot_quicksort(0, len(self.ship_list) - 1)
        elif sort_alg == "Random Pivot Quicksort":
            self.random_pivot_quicksort(0, len(self.ship_list) - 1)
        elif sort_alg == "Three-way Quicksort":
            self.three_way_quicksort(0, len(self.ship_list) - 1)
        elif sort_alg == "Introsort":
            self.introsort(0, len(self.ship_list) - 1)
        elif sort_alg == "Optimized Quicksort":
            self.optimized_quicksort(0, len(self.ship_list) - 1)
        self.update_ship_listbox()
        self.display_movements()
        
    def stable_quicksort(self, low, high):
        if low < high:
            pivot = self.ship_list[high]
            i = low - 1
            for j in range(low, high):
                if self.ship_list[j].num_matroses <= pivot.num_matroses:
                    i += 1
                    self.ship_list[i], self.ship_list[j] = self.ship_list[j], self.ship_list[i]
                    self.movements.append((j, i))
            self.ship_list[i + 1], self.ship_list[high] = self.ship_list[high], self.ship_list[i + 1]
            self.movements.append((high, i + 1))

            pivot_index = i + 1
            self.stable_quicksort(low, pivot_index - 1)
            self.stable_quicksort(pivot_index + 1, high)
    
    def improved_pivot_quicksort(self, low, high):
        if low < high:
            pivot = self.get_improved_pivot(low, high)
            i = low - 1
            for j in range(low, high):
                if self.ship_list[j].num_matroses <= pivot.num_matroses:
                    i += 1
                    self.ship_list[i], self.ship_list[j] = self.ship_list[j], self.ship_list[i]
                    self.movements.append((j, i))
            self.ship_list[i + 1], self.ship_list[high] = self.ship_list[high], self.ship_list[i + 1]
            self.movements.append((high, i + 1))

            pivot_index = i + 1
            self.improved_pivot_quicksort(low, pivot_index - 1)
            self.improved_pivot_quicksort(pivot_index + 1, high)
            
    def get_improved_pivot(self, low, high):
        first = self.ship_list[low]
        middle = self.ship_list[(low + high) // 2]
        last = self.ship_list[high]
        return sorted([first, middle, last])[1]
    
    def random_pivot_quicksort(self, low, high):
        if low < high:
            pivot_idx = random.randint(low, high)
            self.ship_list[pivot_idx], self.ship_list[high] = self.ship_list[high], self.ship_list[pivot_idx]
            pivot = self.ship_list[high]
            i = low - 1
            for j in range(low, high):
                if self.ship_list[j].num_matroses <= pivot.num_matroses:
                    i += 1
                    self.ship_list[i], self.ship_list[j] = self.ship_list[j], self.ship_list[i]
                    self.movements.append((j, i))
            self.ship_list[i + 1], self.ship_list[high] = self.ship_list[high], self.ship_list[i + 1]
            self.movements.append((high, i + 1))

            pivot_index = i + 1
            self.random_pivot_quicksort(low, pivot_index - 1)
            self.random_pivot_quicksort(pivot_index + 1, high)

    def three_way_quicksort(self, low, high):
        if low < high:
            pivot = self.ship_list[high]
            i = low
            while i <= high:
                if self.ship_list[i].num_matroses < pivot.num_matroses:
                    self.ship_list[low], self.ship_list[i] = self.ship_list[i], self.ship_list[low]
                    self.movements.append((i, low))
                    low += 1
                    i += 1
                elif self.ship_list[i].num_matroses == pivot.num_matroses:
                    i += 1
                else:
                    self.ship_list[i], self.ship_list[high] = self.ship_list[high], self.ship_list[i]
                    self.movements.append((i, high))
                    high -= 1

            self.three_way_quicksort(low, high - 1)
            self.three_way_quicksort(i + 1, high)
            
    def introsort(self, low, high, max_depth=None):
        if max_depth is None:
            max_depth = 2 * (high - low + 1).bit_length()

        if low < high:
            if max_depth == 0:
                self.heap_sort(low, high)
                return
            else:
                pivot = self.get_improved_pivot(low, high)
                i = low - 1
                for j in range(low, high):
                    if self.ship_list[j].num_matroses <= pivot.num_matroses:
                        i += 1
                        self.ship_list[i], self.ship_list[j] = self.ship_list[j], self.ship_list[i]
                        self.movements.append((j, i))
                self.ship_list[i + 1], self.ship_list[high] = self.ship_list[high], self.ship_list[i + 1]
                self.movements.append((high, i + 1))

                pivot_index = i + 1
                self.introsort(low, pivot_index - 1, max_depth - 1)
                self.introsort(pivot_index + 1, high, max_depth - 1)
                
    def heap_sort(self, low, high):
        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and self.ship_list[l].num_matroses > self.ship_list[largest].num_matroses:
                largest = l

            if r < n and self.ship_list[r].num_matroses > self.ship_list[largest].num_matroses:
                largest = r

            if largest != i:
                self.ship_list[i], self.ship_list[largest] = self.ship_list[largest], self.ship_list[i]
                self.movements.append((i, largest))
                heapify(n, largest)

        n = high - low + 1
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.ship_list[i], self.ship_list[0] = self.ship_list[0], self.ship_list[i]
            self.movements.append((0, i))
            heapify(i, 0)
            
    def optimized_quicksort(self, low, high):
        while low < high:
            if high - low > 16:
                pivot = self.get_improved_pivot(low, high)
                i = low - 1
                j = high
                while True:
                    i += 1
                    while self.ship_list[i].num_matroses < pivot.num_matroses:
                        i += 1
                    j -= 1
                    while self.ship_list[j].num_matroses > pivot.num_matroses:
                        j -= 1
                    if i >= j:
                        break
                    self.ship_list[i], self.ship_list[j] = self.ship_list[j], self.ship_list[i]
                    self.movements.append((i, j))
                self.ship_list[i], self.ship_list[high] = self.ship_list[high], self.ship_list[i]
                self.movements.append((high, i))

                if i - low < high - i:
                    self.optimized_quicksort(low, i - 1)
                    low = i + 1
                else:
                    self.optimized_quicksort(i + 1, high)
                    high = i - 1
            else:
                for i in range(low, high):
                    min_idx = i
                    for j in range(i + 1, high + 1):
                        if self.ship_list[j].num_matroses < self.ship_list[min_idx].num_matroses:
                            min_idx = j
                    if min_idx != i:
                        self.ship_list[i], self.ship_list[min_idx] = self.ship_list[min_idx], self.ship_list[i]
                        self.movements.append((min_idx, i))
                break

    def display_movements(self):
        self.movements_text.delete(1.0, tk.END)
        for movement in self.movements:
            self.movements_text.insert(tk.END, f"ship#: {movement[0]:2} -> ship# {movement[1]:2}\n")
        
if __name__ == "__main__":
    app = ShipSortGUI()
    app.mainloop()
