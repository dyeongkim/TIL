# 스택(Stack)
한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out) 형식의 자료 구조  
자료를 넣는 것을 **푸쉬**(Push) 꺼내는 것을 **팝**(pop)이라고 한다.

## 시간복잡도
- 검색 : O(n)
- 추가/삭제 : O(1)

## 구현(Python)

```Python
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
```