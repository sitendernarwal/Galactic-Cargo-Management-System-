class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.height = 1  # To keep track of height of a node in AVL tree
        pass