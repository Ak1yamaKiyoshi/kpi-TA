from src.rbtree import RedBlackTree




tree = RedBlackTree()
for i in range(15):
    tree.insert(i*i)
tree.display_highlight()