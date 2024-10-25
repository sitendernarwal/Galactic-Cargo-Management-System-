from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

def update(root, obj, bin_id, delete=False):
    if root is None:
        return None
    if root.element.bin_id == bin_id:
        if delete:
            root.element.remove_object(obj.element.object_id)
        else:
            root.element.add_object(obj)
        return root
    elif root.element.bin_id < bin_id:
        root.right = update(root.right, obj, bin_id, delete)
    else:
        root.left = update(root.left, obj, bin_id, delete)
    return root

def cmp_1(a, b):
    if a.object_id == b.object_id:
        return 0
    elif a.object_id < b.object_id:
        return -1
    else:
        return 1

def cmp_2(a, b):
    if a.capacity == b.capacity:
        if a.bin_id < b.bin_id:
            return -1
        elif a.bin_id > b.bin_id:
            return 1
        else:
            return 0
    elif a.capacity > b.capacity:
        return 1
    else:
        return -1

class tempbin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity

class GCMS:
    def __init__(self):
        self.bin_tree_id = AVLTree()
        self.bin_tree = AVLTree(cmp_2)
        self.object_tree = AVLTree(cmp_1)

    def add_bin(self, bin_id, capacity):
        bin_to_insert = Bin(bin_id, capacity)
        bin_temp = tempbin(bin_id, capacity)
        
        self.bin_tree_id.insert(bin_to_insert)
        self.bin_tree.insert(bin_temp)

    def add_object(self, object_id, size, color):
        def compact_1(root, obj):
            if root is None:
                return None
            if root.element.capacity < obj.size:
                return compact_1(root.right, obj)
            else:
                left_fit = compact_1(root.left, obj)
                return left_fit if left_fit else root

        def compact_2(root, obj):
            if root is None:
                return None
            if root.element.capacity < obj.size:
                return compact_2(root.right, obj)
            left_fit = compact_2(root.left, obj)
            right_fit = None
            if not left_fit:
                right_fit = compact_2(root.right, obj)
            else:
                if left_fit.element.capacity == root.element.capacity:
                    right_fit = compact_2(root.right, obj)
                    if right_fit and right_fit.element.capacity  == root.element.capacity:
                        return right_fit
                    else:
                        return root     
                else:
                     return left_fit
            
            if right_fit and right_fit.element.capacity == root.element.capacity:
                return right_fit
            else:
                return root
            
        def largest_1(root, obj):
            if root is None:
                return None
            if root.element.capacity < obj.size:
                return largest_1(root.right, obj)
            right_fit = largest_1(root.right, obj)
            left_fit = None
            if right_fit is None:
                left_fit = largest_1(root.left, obj)
            else:
                if right_fit.element.capacity == root.element.capacity:
                   left_fit = largest_1(root.left, obj)
                   if  left_fit and left_fit.element.capacity == root.element.capacity:
                       return left_fit
                   else:
                       return root
                else:
                     return right_fit

            if left_fit and left_fit.element.capacity == root.element.capacity:
                return left_fit 
            else:
                return root

        def largest_2(root, obj):
        
            if root is None:
                return None
        
            if root.element.capacity < obj.size:
                return largest_2(root.right, obj)
        
            else:
                right_fit = largest_2(root.right, obj)
                return right_fit if right_fit else root

        obj = Object(object_id, size, color)
        parent = None

        if color == Color.BLUE:
            parent = compact_1(self.bin_tree.root, obj)
        
        elif color == Color.YELLOW:
            parent = compact_2(self.bin_tree.root, obj)
        
        elif color == Color.RED:
            parent = largest_1(self.bin_tree.root, obj)
        
        elif color == Color.GREEN:
            parent = largest_2(self.bin_tree.root, obj)

        if parent is not None:
            obj.parent = parent.element.bin_id
            self.object_tree.insert(obj)
            
            temp = tempbin(parent.element.bin_id, parent.element.capacity - size)
            self.bin_tree.delete(parent.element)
            self.bin_tree.insert(temp)
            # self.bin_tree.inorder()
            self.bin_tree_id.root = update(self.bin_tree_id.root, obj, temp.bin_id)
        else:
            raise NoBinFoundException

    def delete_object(self, object_id):
        def find_object(root, object_id):
            if root is None:
                return None
            if root.element.object_id == object_id:
                return root
            elif root.element.object_id < object_id:
                return find_object(root.right, object_id)
            else:
                return find_object(root.left, object_id)

        def find_parent(root, bin_id):
            if root is None:
                return None
            if root.element.bin_id == bin_id:
                return root
            elif root.element.bin_id < bin_id:
                return find_parent(root.right, bin_id)
            else:
                return find_parent(root.left, bin_id)

        obj = find_object(self.object_tree.root, object_id)
        if obj is not None:
            size = obj.element.size

            parent = find_parent(self.bin_tree_id.root, obj.element.parent)

            temp = tempbin(obj.element.parent, parent.element.capacity - parent.element.current_load)
            self.bin_tree.delete(temp)

            temp = tempbin(obj.element.parent, parent.element.capacity - parent.element.current_load + size)
            self.bin_tree.insert(temp)

            self.bin_tree_id.root = update(self.bin_tree_id.root, obj, obj.element.parent, True)
            self.object_tree.delete(obj.element)
            
    def bin_info(self, bin_id):
        def find_bin(root, bin_id):
            if root is None:
                return None
            if root.element.bin_id == bin_id:
                return root
            elif root.element.bin_id < bin_id:
                return find_bin(root.right, bin_id)
            else:
                return find_bin(root.left, bin_id)

        bin_r = find_bin(self.bin_tree_id.root, bin_id)
        b_objects = []
        def traverse(root):
            if root is not None:
                traverse(root.left)
                b_objects.append(root.element.object_id)
                traverse(root.right)
        if bin_r is not None:
            traverse(bin_r.element.obj_tree.root)
            return (bin_r.element.capacity - bin_r.element.current_load, b_objects) 

    def object_info(self, object_id):
        def find_object(root, object_id):
            if root is None:
                return None
            if root.element.object_id == object_id:
                return root
            elif root.element.object_id < object_id:
                return find_object(root.right, object_id)
            else:
                return find_object(root.left, object_id)

        obj = find_object(self.object_tree.root, object_id)
        return obj.element.parent if obj else None
