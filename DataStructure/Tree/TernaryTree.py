# 삼진트리 구현
class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.mid = None
        self.right = None

class TernaryTree():
    def __init__(self):
        self.root = None

    def add_node(self, value):
        self.root = self.add_node_recursion(self.root, value)

    def add_node_recursion(self, node, value):
        if node is None:
            node = Node(value)
        elif value < node.value:
            node.left = self.add_node_recursion(node.left, value)
        elif value == node.value:
            node.mid = self.add_node_recursion(node.mid, value)
        else :
            node.right = self.add_node_recursion(node.right, value)
        return node
    
    def search(self, value):
        return self.search_recursion(self.root, value)
    
    def search_recursion(self, node, value):
        if node is None:
            return False
        elif value < node.value:
            return self.search_recursion(node.left, value)
        elif value == node.value:
            return True
        else :
            return self.search_recursion(node.right, value)

    def print_tree(self):
        if self.root is not None:
            self.print_tree_recursion(self.root)

    def print_tree_recursion(self, node):
        if node:
            self.print_tree_recursion(node.left)
            print(node.value, end=' ')
            self.print_tree_recursion(node.mid)
            self.print_tree_recursion(node.right)

tree = TernaryTree()

tree.add_node(5)
tree.add_node(4)
tree.add_node(9)
tree.add_node(7)
tree.add_node(2)
tree.add_node(3)

print(tree.search(7)) 
print(tree.search(10))

tree.print_tree()
