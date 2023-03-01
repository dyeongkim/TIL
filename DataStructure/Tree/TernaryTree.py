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

    def add_node(self, node, value):
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
