# 큐 구현
class Queue():
    def __init__(self):
        self.queue = []

    # rear에 위치한 요소 반환
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else :
            return self.queue[0]
        
    # 큐에 요소 삽입
    def enqueue(self, data):
        self.queue.append(data)

    # 큐 rear에 위치한 요소 삭제 후 반환
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else :
            result = self.queue[0]
            self.queue = self.queue[1:]
            return result

    # 큐가 비어있는지 확인
    def isEmpty(self):
        empty = False
        if len(self.queue) == 0 :
            empty = True
        return empty
