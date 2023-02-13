# 큐(Queue)
먼저 집어 넣은 데이터가 먼저 나오는 FIFO(First In First Out) 형식의 자료 구조 

## Queue의 종류
- 선형큐
  - 1차원 배열을 이용해 큐를 구현한다.   
  - 인덱스가 증가만 하는 방식이라 앞부분에 공간이 있어도 활용할 수 없어 비효율적이다.
- 환형큐

## 시간복잡도
- 추가 : O(1)
- 삭제 : O(n)

## 구현(Python)

```Python
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

```