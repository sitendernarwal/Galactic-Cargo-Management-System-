
from avl import AVLTree
def cmp_1(a, b):
    if a.object_id == b.object_id:
        return 0
    elif a.object_id < b.object_id:
        return -1
    else:
        return 1
class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.current_load = 0
        self.obj_tree = AVLTree(cmp_1)
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        object.parent = self.bin_id
        self.current_load += object.size
        self.obj_tree.insert(object)
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        def find_object(root, object_id):
            if root is None:
                return None
            if root.element.object_id == object_id:
                return root
            elif root.element.object_id < object_id:
                return find_object(root.right, object_id)
            else:
                return find_object(root.left, object_id)
        obj = find_object(self.obj_tree.root, object_id)
        size = 0
        if obj:
            size = obj.element.size
            self.obj_tree.delete(obj.element)
            obj.parent = None
        self.current_load -= size
    
