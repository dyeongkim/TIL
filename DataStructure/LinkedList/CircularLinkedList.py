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