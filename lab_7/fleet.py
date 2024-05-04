import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value, node)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value, node)
            else:
                self._insert(value, node.right)

    def find_node(self, value):
        return self._find_node(value, self.root)

    def _find_node(self, value, node):
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self._find_node(value, node.left)
        else:
            return self._find_node(value, node.right)

class PirateGameBST(BinaryTree):
    def __init__(self):
        super().__init__()
        self.ship_nodes = []

    def insert_ship(self, num_sailors):
        self.insert(num_sailors)
        node = self.find_node(num_sailors)
        self.ship_nodes.append(node)

    def defeat_pirates(self, num_pirates):
        ship = self.root
        path = []
        while ship:
            path.append(ship)
            if ship.value >= num_pirates:
                break
            if num_pirates > ship.value:
                ship = ship.right
            else:
                ship = ship.left

        if ship:
            message = f"Ship with {ship.value} sailors will attack the pirates."
            return path, message

        new_ship = Node(num_pirates)
        self.insert(num_pirates)
        self.ship_nodes.append(new_ship)
        message = f"New ship with {num_pirates} sailors created to attack the pirates."
        return path + [new_ship], message

class PirateGameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pirate Game")

        self.tree = PirateGameBST()

        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack(side=tk.LEFT, padx=10)

        self.node_objects = {}
        self.create_node_objects()

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.sailors_entry = ttk.Entry(self.input_frame, validate="key", validatecommand=(self.input_frame.register(self.validate_input), "%P"))
        self.sailors_entry.pack(pady=5)

        self.add_ship_button = ttk.Button(self.input_frame, text="Add Ship", command=self.add_ship)
        self.add_ship_button.pack(pady=5)

        self.pirates_entry = ttk.Entry(self.input_frame, validate="key", validatecommand=(self.input_frame.register(self.validate_input), "%P"))
        self.pirates_entry.pack(pady=5)

        self.attack_button = ttk.Button(self.input_frame, text="Attack Pirates", command=self.attack_pirates)
        self.attack_button.pack(pady=5)

        self.zoom_frame = tk.Frame(self.input_frame)
        self.zoom_frame.pack(pady=5)

        self.zoom_in_button = ttk.Button(self.zoom_frame, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.pack(side=tk.LEFT, padx=5)

        self.zoom_out_button = ttk.Button(self.zoom_frame, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.pack(side=tk.LEFT, padx=5)

        self.message_var = tk.StringVar()
        self.message_label = tk.Label(self.input_frame, textvariable=self.message_var)
        self.message_label.pack(pady=5)

        self.zoom_level = 1.0

    def validate_input(self, input_str):
        return input_str.isdigit() or input_str == ""

    def create_node_objects(self):
        self.canvas.delete("all")
        self.node_objects = {}

        if self.tree.root:
            self.create_node_object(self.tree.root, 400, 50)

    def create_node_object(self, node, x, y):
        node_object = self.canvas.create_oval(x - 20 * self.zoom_level, y - 20 * self.zoom_level,
                                               x + 20 * self.zoom_level, y + 20 * self.zoom_level, fill="lightblue")
        self.canvas.create_text(x, y, text=str(node.value))
        self.node_objects[node] = node_object

        if node.left:
            self.create_node_object(node.left, x - 150 * self.zoom_level, y + 100 * self.zoom_level)
            self.canvas.create_line(x, y + 20 * self.zoom_level, x - 150 * self.zoom_level, y + 80 * self.zoom_level)

        if node.right:
            self.create_node_object(node.right, x + 150 * self.zoom_level, y + 100 * self.zoom_level)
            self.canvas.create_line(x, y + 20 * self.zoom_level, x + 150 * self.zoom_level, y + 80 * self.zoom_level)

    def add_ship(self):
        num_sailors = int(self.sailors_entry.get())
        self.tree.insert_ship(num_sailors)
        self.create_node_objects()

    def attack_pirates(self):
        num_pirates = int(self.pirates_entry.get())
        path, message = self.tree.defeat_pirates(num_pirates)
        self.highlight_path(path)
        self.message_var.set(message)

    def highlight_path(self, path):
        for node_object in self.node_objects.values():
            self.canvas.itemconfig(node_object, fill="lightblue")

        for node in path:
            node_object = self.node_objects.get(node)
            if node_object:
                self.canvas.itemconfig(node_object, fill="green")
                self.master.update()

    def zoom_in(self):
        self.zoom_level *= 1.1
        self.create_node_objects()

    def zoom_out(self):
        self.zoom_level /= 1.1
        self.create_node_objects()

if __name__ == "__main__":
    root = tk.Tk()
    gui = PirateGameGUI(root)
    root.mainloop()