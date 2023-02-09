# 노드 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 링크드 리스트 구현
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
