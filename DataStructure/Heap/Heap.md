# 힙(Heap)
> 최댓값 및 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리(complete binary tree)를 기본으로 한 자료구조


## 힙(Heap)의 종류
- 최대 힙(Max Heap)
    - 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진트리
- 최소 힙(Min Heap)
    - 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진트리

<br>

### 힙 구현(Python)
```Python
# Heap 구현
# 최소 힙
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return(i-1)//2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)
        
    def has_left_child(self, i):
        return self.right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap)-1 # 방금 추가된 key
        while i != 0 and self.heap[self.parent(i)] > self.heap[i] : # 새 key가 부모 키보다 작으면 스왑
            self.swap(i, self.parent(i))
            i = self.parent(i)
# 최대 힙
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return(i-1)//2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def has_left_child(self, i):
        return self.left_child(i) < len(self.heap)
        
    def has_left_child(self, i):
        return self.right_child(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap)-1 # 방금 추가된 key
        while i != 0 and self.heap[self.parent(i)] < self.heap[i] : # 새 key가 부모 키보다 크면 스왑
            self.swap(i, self.parent(i))
            i = self.parent(i)
```
