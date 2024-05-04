import tkinter as tk
import random

class Ship:
    def __init__(self, num_matroses):
        self.num_matroses = num_matroses

    def __str__(self):
        return f"Ship with {self.num_matroses} matroses"

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
        self.sort_alg_var.set("Shell Sort")
        
        self.sort_menu = tk.OptionMenu(self, self.sort_alg_var, "Shell Sort", "Bubble Sort", "Counting Sort")
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
        sort_alg = self.sort_alg_var.get()
        if sort_alg == "Shell Sort":
            self.shell_sort()
        elif sort_alg == "Bubble Sort":
            self.bubble_sort()
        elif sort_alg == "Counting Sort":
            self.counting_sort()
        self.display_movements()
            
    def shell_sort(self):
        n = len(self.ship_list)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.ship_list[i]
                j = i
                while j >= gap and self.ship_list[j - gap].num_matroses > temp.num_matroses:
                    self.ship_list[j] = self.ship_list[j - gap]
                    j -= gap
                    self.movements.append((j - gap, j))
                self.ship_list[j] = temp
            gap //= 2
        
    def bubble_sort(self):
        n = len(self.ship_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.ship_list[j].num_matroses > self.ship_list[j + 1].num_matroses:
                    self.ship_list[j], self.ship_list[j + 1] = self.ship_list[j + 1], self.ship_list[j]
                    self.movements.append((j + 1, j))
                    
    def counting_sort(self):
        max_matroses = max(ship.num_matroses for ship in self.ship_list)
        counts = [[] for _ in range(max_matroses + 1)]
        for i, ship in enumerate(self.ship_list):
            counts[ship.num_matroses].append(i)
        sorted_ships = []
        for i, indices in enumerate(counts):
            for idx in indices:
                sorted_ships.append(self.ship_list[idx])
                self.movements.append((idx, len(sorted_ships) - 1))
        self.ship_list = sorted_ships
        self.update_ship_listbox()

                
    def display_movements(self):
        self.movements_text.delete(1.0, tk.END)
        for movement in self.movements:
            self.movements_text.insert(tk.END, f"ship#: {movement[0]:2} -> ship# {movement[1]:2}\n")
        
if __name__ == "__main__":
    app = ShipSortGUI()
    app.mainloop()
