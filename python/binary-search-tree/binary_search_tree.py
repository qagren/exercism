class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = int(data)
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    def append(self, node):
        if node.data <= self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.append(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.append(node)
        return self

class BinarySearchTree:

    root = None

    def __init__(self, tree_data):
        for d in tree_data:
            self.insert(d)

    def insert(self, d):
        node = TreeNode(d)
        if self.root is None:
            self.root = node
        else:
            self.root.append(node)

    def data(self):
        return self.root

    def sorted_data(self):
        return flatten_node(self.root)


def flatten_node(node, l=None):
    if l is None:
        l = []
    if node is None:
        return l
    smaller = flatten_node(node.left, l)
    smaller.append(str(node.data))
    return flatten_node(node.right, smaller)