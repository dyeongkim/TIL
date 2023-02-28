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