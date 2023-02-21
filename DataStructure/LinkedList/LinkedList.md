# 연결 리스트(Linked List)
> 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료구조.
```Python
# 노드 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
```
<br>

## 장단점
- **장점**
    - 배열에 비해서 원소 추가, 삭제가 빠르다.
    - 임의의 위치에 원소를 추가/삭제 = O(1)

- **단점**
    - 배열에 비해서 검색속도가 느리다
    - 임의의 위치에 있는 원소를 확인/변경 = O(N)


## 단일 연결 리스트
> 각 노드가 자신의 다음 노드의 주소를 가지고 있는 연결 리스트 

### 단일 연결 리스트 구현(Python)
```Python
# 노드 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결 리스트 구현
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    #맨 뒤에 새로운 노드 추가하기
    def add(self, data) :
        node = self.head
        # 마지막 노드까지 검색
        while node.next is not None :
            node = node.next
        
        #마지막 노드 next에 새로운 노드 추가
        node.next = Node(data)

    #노드 검색 O(n)
    def get(self, index) :
        node = self.head
        for i in range(index):
            node = node.next
        return node

    #임의의 위치에 노드 추가 O(1)
    def insert(self, data, index) :
        new_node = Node(data)

        #헤드에 추가할때
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        #임의의 위치에 삽입
        node = self.get(index)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    #노드 삭제 O(1)
    def delete(self, index) :
        if index == 0:
            self.head = self.head.next
            return
        
        node = self.get(index-1)
        node.next = node.next.next
```

## 이중 연결 리스트(Doubly Linked list)
> 각 노드가 자신의 이전 노드와 다음 노드의 주소를 가지고 있는 연결 리스트

### 이중 연결 리스트 구현(Python)
```Python
# 노드 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 연결 리스트 구현
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    #맨 뒤에 새로운 노드 추가하기
    def add(self, data) :
        node = self.head
        # 마지막 노드까지 검색
        while node.next is not None :
            node = node.next
        
        #마지막 노드 next에 새로운 노드 추가
        node.next = Node(data)

    #노드 검색 O(n)
    def get(self, index) :
        node = self.head
        for i in range(index):
            node = node.next
        return node

    #임의의 위치에 노드 추가 O(1)
    def insert(self, data, index) :
        new_node = Node(data)

        #헤드에 추가할때
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        #임의의 위치에 삽입
        node = self.get(index)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    #노드 삭제 O(1)
    def delete(self, index) :
        if index == 0:
            self.head = self.head.next
            return
        
        node = self.get(index-1)
        node.next = node.next.next
```

## 원형 연결 리스트
> 연결 리스트의 끝이 처음과 연결되어 있는 리스트

### 원형 연결 리스트 구현(Python)
```Python
# 원형 연결 리스트 구현
# 노드 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 원형 연결 리스트
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    #비어있는지 체크
    def is_empty(self):
        return self.head is None

    #맨 뒤에 새로운 노드 추가하기
    def append(self, data) :
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
        else :
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

    #노드 검색 O(n)
    def search(self, data) :
        if self.is_empty():
            return None
        cur_node = self.head
        while cur_node.next != self.head:
            if cur_node.data == data:
                return cur_node
            cur_node = cur_node.next
        if cur_node.data == data:
            return cur_node
        return None

    #
    def prepend(self, data) :

    #노드 삭제 O(1)
    def remove(self, data) :
        if self.is_empty():
            return

        #삭제할 대상이 헤드일때
        if self.head.data == data :
            cur_node = self.head
            while cur_node.next == self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next # 마지막 노드의 next를 헤드의 next로 변경
            self.head = self.head.next # 헤드를 헤드 다음 노드로 변경
        else:
            prev_node = self.head
            cur_node = self.head.next
            while cur_node != self.head:
                if cur_node.data == data:
                    prev_node.next = cur_node.next # 이전 노드의 다음 노드를 대상 다음노드로 변경
                    del cur_node # 대상노드 제거
                    return
                #하나씩 이동
                prev_node = cur_node
                cur_node = cur_node.next

    #리스트 목록 출력
    def print_list(self) :
        if self.is_empty():
            return
        cur_node = self.head
        while cur_node.next != self.head:
            print(cur_node.data)
            cur_node = cur_node.next
        print(cur_node.data)
```