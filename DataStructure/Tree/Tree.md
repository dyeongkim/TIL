# 트리(Tree)
한 노드에서 시작해 다른 정점들을 순회하며 자기 자신에게 돌아오는 순환이 없는 연결 그래프   
비선형 계층적 자료구조

![tree](https://user-images.githubusercontent.com/113990279/218428716-1657a98e-6119-4e8f-8fec-98d6c6a02ac4.png)

- 루트(Root) : 부모가 없는 최상위 노드
- 부모 노드(Parent Node) : 자식 노드를 가진 노드 ex) D는 H, I의 부모 노드
- 자식 노드(Child Node) : 부모 노드의 하위 노드 ex) H, I는 D의 자식 노드
- 단말 노드, 잎 노드, 말단 노드(Leaf Node) : 자식 노드가 없는 노드
- 내부 노드(Internal Node) : 잎 노드가 아닌 노드
- 간선(Edge) : 노드와 노드 간의 연결선
- 형제(Siblings) : 같은 부모 노드를 가지는 노드
- 깊이(Depth) : 루트에서 특정 노드까지 거치는 간선의 수
- 높이(Height) : 루트 노드에서 가장 먼 노드까지 간선의 수
- 레벨(Level) : 특정 깊이를 가지는 노드의 집합
- 차수(degree) : 노드의 자식 수

## Tree의 종류
- 이진트리 : 각 노드가 최대 2개의 자식노드를 갖는 트리
  - 완전 이진 트리(Complete Binary Tree)
    - 마지막을 제외하고 모든 레벨이 완전히 채워져 있다.
    - 마지막 레벨은 꽉 채우지 않아도 노드가 왼쪽에서 오른쪽으로 채워져야 한다.
    - 구현은 배열로 하는것이 일반적이다.
  - 전 이진 트리(Full Binary Tree) : 모든 노드가 0개 또는 2개의 자식 노드를 갖는 트리
  - 포화 이진 트리(Perfect Binary Tree) 
    - 모든 레벨이 노드로 꽉 채워진 트리
    - 모든 말단 노드가 동일한 깊이, 레벨을 갖는다.
    - 트리의 노드의 개수가 2^h(높이)-1 개 이다.
- 삼진트리(Ternary Tree)
    - 
- B-트리
- AVL 트리
- 트라이 트리(Trie Tree)
- 힙 트리(Heap Tree)

## 시간복잡도
- 검색
  - 최소 : O(logn)
  - 최대 : O(n)

## 이진트리 구현(Python)

```Python
# 트리 구현
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
```



## 삼진트리 구현(Python)

```Python
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
```