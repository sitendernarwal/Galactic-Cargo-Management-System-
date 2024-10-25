from node import Node

def comp_1(node_1, node_2):
    if node_1.bin_id == node_2.bin_id:
        return 0
    elif node_1.bin_id < node_2.bin_id:
        return -1
    else:
        return 1

def get_height(root):
    if root is None:
        return 0
    return root.height

def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)

def get_inorder_successor(root):
    if root is None:
        return None
    temp = root.right
    while temp and temp.left:
        temp = temp.left
    return temp

def left_rotation(root):
    new_root = root.right

    root.right = new_root.left
    
    new_root.left = root
    
    root.height = max(get_height(root.left), get_height(root.right)) + 1
    new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1
    
    return new_root

def right_rotation(root):
    new_root = root.left
    
    root.left = new_root.right
    
    new_root.right = root
    
    root.height = max(get_height(root.left), get_height(root.right)) + 1
    new_root.height = max(get_height(new_root.left), get_height(new_root.right)) + 1
    
    return new_root

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def insert(self, element):
        def insert_util(root, element):
            if root is None:
                return Node(element)

            if self.comparator(element, root.element) < 0:
                root.left = insert_util(root.left, element)
            elif self.comparator(element,root.element) > 0:
                root.right = insert_util(root.right, element)

            root.height = max(get_height(root.left), get_height(root.right)) + 1
            balance = get_balance(root)

            if balance > 1 and self.comparator(element, root.left.element) < 0:
                return right_rotation(root)
            if balance > 1 and self.comparator(element, root.left.element) > 0:
                root.left = left_rotation(root.left)
                return right_rotation(root)
            if balance < -1 and self.comparator(element, root.right.element) > 0:
                return left_rotation(root)
            if balance < -1 and self.comparator(element, root.right.element) < 0:
                root.right = right_rotation(root.right)
                return left_rotation(root)

            return root

        self.root = insert_util(self.root, element)
        self.size += 1

    def delete(self, element):
        def delete_util(root, element):
            if root is None:
                return root

            if self.comparator(element, root.element) < 0:
                root.left = delete_util(root.left, element)
            elif self.comparator(element, root.element) > 0:
                root.right = delete_util(root.right, element)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                temp = get_inorder_successor(root)
                root.element = temp.element
                root.right = delete_util(root.right, temp.element)

            root.height = max(get_height(root.left), get_height(root.right)) + 1
            balance = get_balance(root)

            if balance > 1 and get_balance(root.left) >= 0:
                return right_rotation(root)
            if balance > 1 and get_balance(root.left) < 0:
                root.left = left_rotation(root.left)
                return right_rotation(root)
            if balance < -1 and get_balance(root.right) <= 0:
                return left_rotation(root)
            if balance < -1 and get_balance(root.right) > 0:
                root.right = right_rotation(root.right)
                return left_rotation(root)

            return root

        self.root = delete_util(self.root, element)
        if self.root is not None:
            self.size -= 1

    def search(self, element):
        def search_util(root, element):
            if root is None or self.comparator(element, root.element) == 0:
                return root
            if self.comparator(element, root.element) < 0:
                return search_util(root.left, element)
            return search_util(root.right, element)

        return search_util(self.root, element)
    def inorder(self):
        def inorder_util(root):
            if root is None:
                return
            inorder_util(root.left)
            print(f"capacity of {root.element.bin_id} is {root.element.capacity}.")
            inorder_util(root.right)

        inorder_util(self.root)