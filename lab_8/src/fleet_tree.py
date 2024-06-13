from src.bst import BinarySearchTree
from src.rbtree import RedBlackTree, Node

import numpy as np
import copy


class FleetTree(RedBlackTree):
    def __init__(self):
        super().__init__()
        

    def get_ship_size(self:RedBlackTree, target:int):
        """ Calculates ship size to add to tree """
        nodes = self.preorder()
        nodes = [n.value for n in nodes]
        
        new = target - self.max_sum()
        print(f"max sum {self.max_sum()}")
        if new > 0:
            self.insert(new)
            paths = self.get_all_paths()
            new_errors =[abs(target - sum([n.value for n in path if not n.value is None])) for path in paths]
            best_error_index = np.argmin(new_errors)
            local_least_error = new_errors[best_error_index]
            best_local_path = paths[best_error_index]
            
        
        if self.max_sum() >= target:
            errors = list()
            paths =  list()
            for path in self.get_all_paths():
                errors.append(target - sum([n.value for n in path]))
                paths.append(path)
            errors = list(map(lambda x: -np.inf if x >0 else x, errors))
            min_error_idx = np.argmax(errors)
            return None, paths[min_error_idx]

        return new, best_local_path if new > 0 else None
    