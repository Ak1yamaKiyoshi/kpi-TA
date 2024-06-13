import tkinter as tk
from tkinter import ttk
from src.fleet_tree import FleetTree
import random as rd

class TreeVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tree Visualizer")
        self.geometry("800x600")

        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        self.input_field = tk.Entry(input_frame)
        self.input_field.insert(0, "1") 

        self.input_field.pack(side=tk.LEFT)

        submit_button = tk.Button(input_frame, text="Submit", command=self.submit_input)
        submit_button.pack(side=tk.LEFT, padx=10)

        self.canvas = tk.Canvas(self, width=1200, height=500, bg="white")
        self.canvas.pack(pady=10)

        self.tree = FleetTree()

        initial_tree_arr = [rd.randint(50, 200) for i in range(rd.randint(1, 5))]
        for ship in initial_tree_arr:
            self.tree.insert(ship)

        self.canvas.delete("all")
        self.draw_tree([])

    def submit_input(self):
        pirate_ship = eval(self.input_field.get())
        
        _, path = self.tree.get_ship_size(pirate_ship)
        
        self.canvas.delete("all")
        self.draw_tree(path)

    def draw_tree(self, path=None, highlight=None):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        node_radius = 20
        horizontal_spacing = 150
        vertical_spacing = 50
        self.draw_node(self.tree.get_root(), canvas_width // 2, 20, node_radius, highlight)
        self.draw_subtree(self.tree.get_root(), canvas_width // 2, 20, horizontal_spacing, vertical_spacing, node_radius, path, highlight)

    def draw_node(self, node, x, y, radius, highlight=None):
        if node:
            if node.value == highlight:
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="red", width=2)
            else:
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius)
            self.canvas.create_text(x, y, text=str(node.value))

    def draw_subtree(self, node, x, y, horizontal_spacing, vertical_spacing, radius, path, highlight):
        if node:
            self.draw_node(node, x, y, radius, highlight)
            if path and node in path:
                self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="yellow")
                self.canvas.create_text(x, y, text=str(node.value))
            left_x = x - horizontal_spacing
            left_y = y + vertical_spacing
            right_x = x + horizontal_spacing
            right_y = y + vertical_spacing

            if node.left:
                self.draw_subtree(node.left, left_x, left_y, horizontal_spacing // 2, vertical_spacing, radius, path, highlight)
            if node.right:
                self.draw_subtree(node.right, right_x, right_y, horizontal_spacing // 2, vertical_spacing, radius, path, highlight)


if __name__ == "__main__":
    app = TreeVisualizer()
    app.submit_input()
    app.mainloop()
