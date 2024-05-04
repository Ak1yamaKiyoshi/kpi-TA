import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class RBNode:
    def __init__(self, key, color="Red"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.nil = RBNode(None, color="Black")
        self.root = self.nil

    def insert(self, key):
        new_node = RBNode(key)
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = "Red"
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == "Red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "Red":
                    node.parent.color = "Black"
                    uncle.color = "Black"
                    node.parent.parent.color = "Red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "Black"
                    node.parent.parent.color = "Red"
                    self.left_rotate(node.parent.parent)
        self.root.color = "Black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

class Fleet:
    def __init__(self):
        self.tree = RedBlackTree()
        self.root = None
        self.admiral_ship = None

    def add_ship(self, sailors):
        if sailors < 0:
            return
        self.tree.insert(sailors)
        if self.root is None:
            self.root = self.tree.root


    def find_ship_for_attack(self, attackers):
        current = self.root
        while current is not None:
            if not current.key or not attackers:
                return
            if current.key >= attackers:
                return current
            elif attackers > current.key and current.right:
                current = current.right
            elif attackers < current.key and current.left:
                current = current.left
            else:
                break 
        return None

def attack():
    attackers = simpledialog.askinteger("Input", "Enter number of pirates:")
    if attackers is None:
        return
    attacking_ship = fleet.find_ship_for_attack(attackers)
    if attacking_ship is None:
        messagebox.showinfo("No suitable ship", "No ship available for attack.")
    else:
        messagebox.showinfo("Ship for Attack", f"Ship with {attacking_ship.key} sailors selected for attack.")
        update_visualization(attacking_ship)

def add_ship():
    sailors = simpledialog.askinteger("Input", "Enter number of sailors:")
    if sailors is None:
        return
    fleet.add_ship(sailors)
    update_visualization()

def update_visualization(attacking_ship=None):
    canvas.delete("all")
    draw_tree(canvas, 400, 50, fleet.tree.root, attacking_ship)

def draw_tree(canvas, x, y, node, attacking_ship=None, x_offset=200, y_offset=50):
    if node.key is not None:
        if node.left is not None and node.left.key is not None:
            canvas.create_line(x, y, x - x_offset, y + y_offset, fill="black")
            draw_tree(canvas, x - x_offset, y + y_offset, node.left, attacking_ship, x_offset / 2, y_offset)
        if node.right is not None and node.right.key is not None:
            canvas.create_line(x, y, x + x_offset, y + y_offset, fill="black")
            draw_tree(canvas, x + x_offset, y + y_offset, node.right, attacking_ship, x_offset / 2, y_offset)
        fill_color = "red" if node.color == "Red" else "black"
        if attacking_ship and node.key == attacking_ship.key:
            fill_color = "yellow"
        canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=fill_color)
        canvas.create_text(x, y, text=str(node.key), fill="white" if fill_color == "black" else "black")


if __name__ == "__main__":
    fleet = Fleet()

    root = tk.Tk()
    root.title("Naval Fleet")

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    add_ship_button = tk.Button(root, text="Add Ship", command=add_ship)
    add_ship_button.pack()

    attack_button = tk.Button(root, text="Attack", command=attack)
    attack_button.pack()

    root.mainloop()
