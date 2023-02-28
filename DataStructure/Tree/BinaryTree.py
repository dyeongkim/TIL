# 이진트리 구현
class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def add_node(self,value):
        node = Node(value)
        if self.root is None :
            self.root = node
        else :
            self.add_node_recursion(self.root, node)

    def add_node_recursion(self, cur_node, new_node) :
        if new_node.value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = new_node
            else:
                self.add_node_recursion(cur_node.left, new_node)
        else:
            if cur_node.right is None:
                cur_node.right = new_node
            else :
                self.add_node_recursion(cur_node.right, new_node)

    def print_tree(self):
        if self.root is None:
            self.print_tree_recursion
    
    def print_tree_recursion(self, cur_node):
        if cur_node is not None:
            self.print_tree_recursion(cur_node.left)
            print(str(cur_node.value))
            self.print_tree_recursion(cur_node.right)