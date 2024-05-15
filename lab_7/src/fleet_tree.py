from src.bst import BinarySearchTree
import numpy as np
import copy

class FleetTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
    
    @property
    def root(self):
        return self.__root

    def get_ship_size(self, target:int):
        """ Calculates ship size to add to tree """
        print(self)
        print(self.max_sum(), target)

        if self.max_sum() >= target:
            errors = list()
            paths =  list()
            for path in self.get_all_paths():
                errors.append(target - sum([n.value for n in path]))
                paths.append(path)

            errors = list(map(lambda x: -np.inf if x >0 else x, errors))
            #print(paths)
            #print(self)
            min_error_idx = np.argmax(errors)
            #print(paths[min_error_idx])
            return {
                    "new_ship": None,
                    "path": paths[min_error_idx],
                    "error": errors[min_error_idx],
                    "tree": self
                }

        print("GONE MAD ")
        trees =  list()
        errors = list()
        paths =  list()
        for path in self.get_all_paths():
            error = target - sum([n.value for n in path])
            tree_copy =  self.copy()
            tree_copy.insert(error)
            paths.append(path)
            trees.append(tree_copy)
            errors.append(error)

        least_error_tree = None
        least_error_path = None
        least_error = None
        added_element = None
        for tree, error in zip(trees, errors):
            paths = tree.get_all_paths()
            new_errors =[abs(target - sum([n.value for n in path])) for path in paths]
            best_error_index = np.argmin(new_errors)
            local_least_error = new_errors[best_error_index]
            best_local_path = paths[best_error_index]
            if least_error_tree is None or least_error > local_least_error:
                least_error = local_least_error
                least_error_path = best_local_path
                least_error_tree = tree
                added_element = error


        return {
            "new_ship": added_element,
            "path": least_error_path,
            "error": least_error,
            "tree": least_error_tree
        }
