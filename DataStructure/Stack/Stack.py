# 스택 구현
class Stack():
    def __init__(self):
        self.stack = []

    # 가장 마지막 원소 리턴
    def top(self):
        return self.stack[-1]

    # 스택 맨 뒤 요소 추가
    def push(self, data):
        self.stack.append(data)

    # 스택 맨 뒤 요소 리턴 후 삭제
    def pop(self):
        data = None
        if not self.isEmpty(): # 스택이 비어있는지 체크
            return self.stack.pop()
        else :
            print("Stack is Empty")

    # 스택이 비어있는지 확인
    def isEmpty(self):
        if len(self.stack) == 0: # 비어있으면 True
            print("Stack is Empty")
            return True
        else :
            return False
