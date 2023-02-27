# 트리 구현
class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def add_node(self,value):
        node = Node(value)
        if self.root is None :
            self.root = node
        else :
            self._add_node_helper(self.root, node)

    def _add_node_helper(self, cur_node, new_node) :
        if new_node.value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = new_node
            else:
                self._add_node_helper(cur_node.left, new_node)
        else:
            if cur_node.right is None:
                cur_node.right = new_node
            else :
                self._add_node_helper(cur_node.right, new_node)