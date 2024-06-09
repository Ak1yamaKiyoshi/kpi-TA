from src.bucket_sort import bucket_sort
from src.lsd_radix import lsd_radixsort
# MSD - угрупування;
import numpy as np
""" 
"""


import tkinter as tk
import random

class Ship:
    def __init__(self, num_matroses):
        self.num_matroses = num_matroses

    def __str__(self):
        return f"Ship with {self.num_matroses} matroses"

class ShipSortGUI(tk.Tk):
    
    def set_logging(self, logging):
        self.movements = logging
    
    
    def set_shiplist(self, array):
        self.ship_list = array
    
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
        self.sort_alg_var.set("lsd sorting")
        
        self.sort_menu = tk.OptionMenu(self, self.sort_alg_var, "lsd sorting", "bucket sort")
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
    
    @staticmethod
    def arr2ship( array):
        return [Ship(n) for n in array]
    
    @staticmethod
    def ship2arr( ships):
        return [n.num_matroses for n in ships]

    def shuffle_ships(self):
        random.shuffle(self.ship_list)
        self.update_ship_listbox()
        
    def update_ship_listbox(self):
        self.ship_listbox.delete(0, tk.END)
        for ship in self.ship_list:
            self.ship_listbox.insert(tk.END, str(ship))

    def sort_ships(self):
        self.movements = []
        
        if sorted(self.ship2arr(self.ship_list)) == self.ship2arr(self.ship_list):
            self.display_movements()
            self.update_ship_listbox()
            return
        array = self.ship2arr(self.ship_list)
        sort_alg = self.sort_alg_var.get()
        if sort_alg == "lsd sorting":
            array = lsd_radixsort(array, self.movements)
        elif sort_alg == "bucket sort":
            digits = 10**len(str(np.max(array)))
            array = (np.array(array)/digits).tolist()
            array = bucket_sort(array, self.movements)
            array = (np.array(array)*digits).astype(int).tolist()

        self.set_shiplist(self.arr2ship(array))
        self.display_movements()
        self.update_ship_listbox()

    def display_movements(self):
        self.movements_text.delete(1.0, tk.END)
        for movement in self.movements:
            self.movements_text.insert(tk.END, f"\n{movement}")
        
if __name__ == "__main__":
    app = ShipSortGUI()
    app.mainloop()
