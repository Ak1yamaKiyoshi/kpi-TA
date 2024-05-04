import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, value, color='RED'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
        self.left_neighbor = None
        self.right_neighbor = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        self.root = self._insert(self.root, node)
        self.root.color = 'BLACK'

    def _insert(self, root, node):
        if root is None:
            return node

        if node.value < root.value:
            root.left = self._insert(root.left, node)
            root.left.parent = root
        else:
            root.right = self._insert(root.right, node)
            root.right.parent = root

        root = self._rebalance(root)
        return root


    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

        return right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        left_child.right = node
        node.parent = left_child

        return left_child