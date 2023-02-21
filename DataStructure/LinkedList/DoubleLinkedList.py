# 이중 연결 리스트 구현
# 노드 정의
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# 이중 연결 리스트
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #비어있는지 체크
    def is_empty(self):
        return self.head is None

    #맨 뒤에 새로운 노드 추가하기
    def append(self, data) :
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else :
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    #노드 검색 O(n)
    def search(self, index) :
        node = self.head
        for i in range(index):
            node = node.next
        return node

    #노드 삭제 O(1)
    def remove(self, index) :
        if index == 0:
            self.head = self.head.next
            return
        
        node = self.search(index-1)
        node.next = node.next.next
    
    #리스트 목록 출력
    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next