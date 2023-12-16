class NodeBT:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def append(self, key):
        if self.root is None:
            self.root = NodeBT(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = NodeBT(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = NodeBT(key)
            else:
                self._insert_recursive(current_node.right, key)
        else:
            return
    
    def print_tree(self):
        values = []
        self._print_tree_recursive(self.root, values)
        print(", ".join(map(str, values)))

    def _print_tree_recursive(self, current_node, values):
        if current_node is not None:
            self._print_tree_recursive(current_node.left, values)
            values.append(current_node.value)
            self._print_tree_recursive(current_node.right, values)