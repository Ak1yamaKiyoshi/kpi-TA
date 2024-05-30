import tkinter as tk
import random
update=sorted




def partition_threway(arr, first, last, start, mid):
     
    pivot = arr[last]
    end = last
     
    # Iterate while mid is not greater than end.
    while (mid[0] <= end):
         
        # Inter Change position of element at the starting if it's value is less than pivot.
        if (arr[mid[0]] < pivot):
             
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
             
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
             
        # Inter Change position of element at the end if it's value is greater than pivot.
        elif (arr[mid[0]] > pivot):
             
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
             
            end = end - 1
             
        else:
            mid[0] = mid[0] + 1
 
 
 
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

    def __repr__(self) -> str:
        return str(self.num_matroses)


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
        
    def introsort(self, *args):
        
        maxdepth = (len(self.ship_list).bit_length() - 1)*2
        self.introsort_helper(self.ship_list, 0, len(self.ship_list), maxdepth)
    
 
    def update_ship_listbox(self):
        self.ship_listbox.delete(0, tk.END)
        update(self.ship_list)
        for ship in self.ship_list:
            self.ship_listbox.insert(tk.END, str(ship))
        
    def sort_ships(self):
        self.movements = []  
        self.update_ship_listbox()
        sort_alg = self.sort_alg_var.get()

        if sorted(self.ship_list.copy()) == self.ship_list:
            self.update_ship_listbox() 
            self.movements = []
            self.display_movements()    
        else:
            if sort_alg == "Stable Quicksort":
                self.stable_quicksort(0, len(self.ship_list) - 1)
            elif sort_alg == "Improved Pivot Quicksort":
                self.improved_pivot_quicksort(0, len(self.ship_list) - 1)
            elif sort_alg == "Random Pivot Quicksort":
                self.random_pivot_quicksort(0, len(self.ship_list) - 1)
            elif sort_alg == "Three-way Quicksort":
                self.three_way_quicksort(0, len(self.ship_list) - 1)
            elif sort_alg == "Introsort":
                self.introsort(self.ship_list, 0, len(self.ship_list) - 1)
            elif sort_alg == "Optimized Quicksort":
                self.optimized_quicksort(0, len(self.ship_list) - 1)

            update(self.ship_list)
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
            print(f"Sorting subarray: {self.ship_list[low:high+1]}")
            pivot = self.get_improved_pivot(low, high)
            print(f"Pivot: {pivot.num_matroses}")
            i = low - 1
            for j in range(low, high):
                if self.ship_list[j].num_matroses < pivot.num_matroses:
                    i += 1
                    self.ship_list[i], self.ship_list[j] = self.ship_list[j], self.ship_list[i]
                    self.movements.append((j, i))
            self.ship_list[i + 1], self.ship_list[high] = self.ship_list[high], self.ship_list[i + 1]
            self.movements.append((high, i + 1))

            pivot_index = i + 1
            self.improved_pivot_quicksort(low, pivot_index - 1)
            self.improved_pivot_quicksort(pivot_index + 1, high)
        else:
            print(f"Base case: {self.ship_list[low:high+1]}")
            
    def get_improved_pivot(self, low, high):
        subarray = sorted(self.ship_list[low:high+1], key=lambda ship: ship.num_matroses)
        median_index = (high - low + 1) // 2
        return subarray[median_index]
        
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

    def three_way_quicksort(self, first,last):
    # First case when an array contain only 1 element
        if (first >= last): 
            return
        
        # Second case when an array contain only 2 elements
        if (last == first + 1):
            
            if (self.ship_listarr[first] > self.ship_list[last]):
                
                self.ship_list[first], self.ship_list[last] = self.ship_list[last], self.ship_list[first]
                self.movements.append((first, last))
                
                return
    
        # Third case when an array contain more than 2 elements
        start = [first]
        mid = [first]
    
        # Function to partition the array.
        partition_threway(self.ship_list, first, last, start, mid)
        
        # Recursively sort sublist containing elements that are less than the pivot.
        self.stable_quicksort(first, start[0] - 1)
    
        # Recursively sort sublist containing elements that are more than the pivot
        self.stable_quicksort(mid[0], last)
                
    
    
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



    def introsort_helper(self, alist, start, end, maxdepth):
        if end - start <= 1:
            return
        elif maxdepth == 0:
            self.heapsort(alist, start, end)
        else:
            p = self.partition(alist, start, end)
            self.introsort_helper(alist, start, p + 1, maxdepth - 1)
            self.introsort_helper(alist, p + 1, end, maxdepth - 1)
    
    def partition(self, alist, start, end):
        pivot = alist[start]
        i = start - 1
        j = end
    
        while True:
            i = i + 1
            while alist[i] < pivot:
                i = i + 1
            j = j - 1
            while alist[j] > pivot:
                j = j - 1
    
            if i >= j:
                return j
    
            self.swap(alist, i, j)
    
    def swap(self, alist, i, j):
        self.movements.append((i, j))
        alist[i], alist[j] = alist[j], alist[i]
    
    def heapsort(self, alist, start, end):
        self.build_max_heap(alist, start, end)
        for i in range(end - 1, start, -1):
            self.swap(alist, start, i)
            self.max_heapify(alist, index=0, start=start, end=i)
            
    
    def build_max_heap(self, alist, start, end):
        def parent(i):
            return (i - 1)//2
        length = end - start
        index = parent(length - 1)
        while index >= 0:
            self.max_heapify(alist, index, start, end)
            index = index - 1
    
    def max_heapify(self, alist, index, start, end):
        def left(i):
            return 2*i + 1
        def right(i):
            return 2*i + 2
    
        size = end - start
        l = left(index)
        r = right(index)
        if (l < size and alist[start + l] > alist[start + index]):
            largest = l
        else:
            largest = index
        if (r < size and alist[start + r] > alist[start + largest]):
            largest = r
        if largest != index:
            self.swap(alist, start + largest, start + index)
            
            self.max_heapify(alist, largest, start, end)
    
    

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
    app.mainloop()# 