from src.node import Node
import random as rd

#BST
class BinarySearchTree: 
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def insert(self, value):
        if (self.__root == None):
            self.__root = Node(value=value, parent=None)
            return
        pointer = self.__root
        while True:
            if value < pointer.value and pointer.left:
                pointer = pointer.left
            elif value >= pointer.value and pointer.right:
                pointer = pointer.right
            else: break

        if pointer.value > value: pointer.left = Node(value, pointer)
        else: pointer.right = Node(value, pointer)

    def copy(self):
        new_tree = self.__class__()
        if self.__root:
            new_tree.__root = self._copy_tree(self.__root)
        return new_tree

    def _copy_tree(self, node):
        if node:
            new_node = Node(node.value)
            new_node.left = self._copy_tree(node.left)
            new_node.right = self._copy_tree(node.right)
            if new_node.left:
                new_node.left.parent = new_node
            if new_node.right:
                new_node.right.parent = new_node
            return new_node
        else:
            return None
        
        
    def remove(self, value):
        def min(pointer):
            while pointer.left:
                pointer = pointer.left
            return pointer

        pointer = self.binarySearch(value)

        if not pointer:
            return

        if pointer == self.__root:  # If the node to be removed is the root
            if pointer.left and pointer.right:
                ptr = min(pointer.right)
                pointer.value = ptr.value
                if ptr == ptr.parent.left:
                    ptr.parent.left = None
                else:
                    ptr.parent.right = None
            elif pointer.left:
                self.__root = pointer.left
            elif pointer.right:
                self.__root = pointer.right
            else:
                self.__root = None
            return

        parent = pointer.parent
        if parent.left == pointer:
            atr = "left"
        else:
            atr = "right"

        if pointer.left and pointer.right:
            ptr = min(pointer.right)
            pointer.value = ptr.value
            if ptr == ptr.parent.left:
                ptr.parent.left = None
            else:
                ptr.parent.right = None
        elif pointer.left:
            setattr(parent, atr, pointer.left)
            pointer.left.parent = parent
        elif pointer.right:
            setattr(parent, atr, pointer.right)
            pointer.right.parent = parent
        else:
            setattr(parent, atr, None)
            
   # Turn tree to array by pre order traversal
    def pre_order_to_array(self, pointer=False):
        if pointer == False: pointer = self.__root
        out = []
        
        out.append(pointer.value)        
        if pointer.left: out += self.pre_order_to_array(pointer.left) 
        if pointer.right: out += self.pre_order_to_array(pointer.right) 

        return out  


    # Turn tree to array by in order traversal
    def in_order_to_array(self, pointer=False):
        if pointer == False: pointer = self.__root
        out = []
 
        if pointer.left: out += self.in_order_to_array(pointer.left) 
        out.append(pointer.value)        
        if pointer.right: out += self.in_order_to_array(pointer.right) 

        return out  


    # Turn tree to array by post order traversal
    def post_order_to_array(self, pointer=False):
        if pointer == False: pointer = self.__root
        out = []
        
        if pointer.left: out += self.post_order_to_array(pointer.left) 
        if pointer.right: out += self.post_order_to_array(pointer.right) 
        out.append(pointer.value)        

        return out  

  

        return out
    def binarySearch(self, value, pointer=False):
        if pointer==False:
            pointer = self.__root
        
        if not pointer:
            return
        if pointer.value == value:
            return self.__root
        while True:
            if pointer.value>value and pointer.left!=None:
                pointer = pointer.left
            elif pointer.value<value and pointer.right != None:
                pointer = pointer.right
            else: 
                break
        if pointer.value == value:
            return pointer


    # Turn tree to array by pre-order traversal
    def pre_order_to_array(self, pointer=False):
        if pointer == False:
            pointer = self.__root
        out = []
        
        if pointer is None:  # Check if pointer is None
            return out  # Return an empty list if the tree is empty

        out.append(pointer.value)
        if pointer.left:
            out += self.pre_order_to_array(pointer.left)
        if pointer.right:
            out += self.pre_order_to_array(pointer.right)

        return out

    def in_order_to_array(self, pointer=False):
        if pointer == False:
            pointer = self.__root
        out = []

        if pointer is None:
            return out

        if pointer.left is not None:
            out += self.in_order_to_array(pointer.left)
        out.append(pointer.value)
        if pointer.right is not None:
            out += self.in_order_to_array(pointer.right)

        return out

    # Turn tree to array by post-order traversal
    def post_order_to_array(self, pointer=False):
        if pointer == False:
            pointer = self.__root
        out = []

        if pointer is None:  # Check if pointer is None
            return out  # Return an empty list if the tree is empty

        if pointer.left is not None:  # Check if left child exists
            out += self.post_order_to_array(pointer.left)
        if pointer.right is not None:  # Check if right child exists
            out += self.post_order_to_array(pointer.right)
        out.append(pointer.value)

        return out


    def __add__(self, lst):
        for i in lst:
            self.insert(i)


    def __str__(self):
        return self.__repr__()


    def __eq__(self, __o: object) -> bool:
        return self.in_order_to_array() == __o.in_order_to_array()


    def __len__(self):
        return len(self.in_order_to_array())


    def height(self, pointer=False, height=False):
        if pointer == False: pointer = self.__root
        elif not pointer: return height
        if height == False: height = 0
        left = self.height(pointer.left, height+1)
        right = self.height(pointer.right, height+1)
        return max(left, right)


    # To clearly see which number to remove
    def display_highlight(self, to_remove=None, pointer=False, space=0, level=4):
        if pointer == False: pointer = self.__root
        if (pointer == None): return
        space += level
        self.display_highlight(to_remove, pointer.right, space)
        for i in range(level, space): print(end = '\033[92m' + " ")  
        if pointer.value != to_remove:
            print('\033[93m' + "[" + '\033[0m' + str(pointer.value) + '\033[93m' + "]<")
        else: 
            print('\033[93m' + "[" + '\033[91m' + str(pointer.value) + '\033[93m' + "]<")
        self.display_highlight(to_remove, pointer.left, space)
        print("" + '\033[0m', end="")


    # In Order Traversal Print 
    def display(self, pointer=False, space=0, level=4):
        if pointer == False: pointer = self.__root
        if not pointer: return
        space += level
        self.display(pointer.right, space)

        for i in range(level, space): print(end = ".")  
        print("[" + str(pointer.value) + "]<")
        self.display(pointer.left, space)
        print("", end="")


    def __repr__(self, pointer=False):
        if pointer == False: pointer = self.__root
        out = ""
        
        if pointer.left: out += self.__repr__(pointer.left) 
        out += str(pointer.value) + " "        
        if pointer.right: out += self.__repr__(pointer.right) 

        return out  


    def max_sum(self, pointer=False, summ=False):
        if pointer == False: pointer = self.__root
        elif not pointer: return summ
        if summ == False: summ = 0
        left = self.max_sum(pointer.left, summ+pointer.value)
        right = self.max_sum(pointer.right, summ+pointer.value)
        return max(left, right)


    def get_all_paths(self, pointer=False, path=None, complete_paths=None):
        if path is None:
            path = list() 
        if complete_paths is None:
            complete_paths = list()
        if pointer is False:
            pointer = self.__root
        complete_paths.append(path.copy())

        if pointer:
            self.get_all_paths(pointer.left, path + [pointer], complete_paths)
            self.get_all_paths(pointer.right, path + [pointer], complete_paths)
        return complete_paths
            
