# 너비 우선 탐색/Breadth-first search(BFS)
> 노드에서 인접한 노드를 먼저 탐색하는 방법   
구현할때 Queue를 사용   
인접한 노드를 Queue에 담고 하나씩 pop하며 다음 노드에서 다시 인접한 노드를 담는 식으로 구현한다.
<br>

## 장단점
- **장점**
    - 두 노드 사이의 최단 경로를 찾을수있다.

- **단점**
    - DFS에 비해서 메모리 요구 사항이 높다.
    - 규모가 크고 밀도가 높은 그래프에서 DFS보다 느림
    - 가중 그래프에서 최단 경로를 찾는데 효율적이지 않음

## BFS 구현(Python)
- 방문할 노드 대기열(Queue)을 만들고 시작 노드를 넣는다.
- 방문한 노드를 위한 목록(visited)을 만든다.
- 대기열에 노드가 들어있는 경우 반복 :
    - 대기열에서 노드 꺼내기
    - 방문하지 않은 노드인경우 :
        - 방문한 목록에 넣는다.
        - 인접한 모든 노드를 대기열에 저장


```Python
# BFS 구현
from collections import deque

class Graph:
    def __init__(self):
        self.list = {}

    #노드간 간선 추가
    def add_edge(self, u, v):
        if u not in self.list:
            self.list[u] = []
        self.list[u].append(v)
        '''
        #무방향 그래프일경우 추가
        if v not in self.list:
            self.list[v] = []
        self.list[v].append(u)
        '''

    def bfs(self, start):
        visited = set()

        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:

            vertex = queue.popleft()
            print(vertex, end=' ')

            if vertex in self.list: # 단말노드일경우 에러 처리
                for neighbor in self.list[vertex]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)

graph.bfs(0)
```

## BFS 연습문제
- 기본
    - [백준 1926 - 그림](https://www.acmicpc.net/problem/1926)
        - [풀이](/Algorithm/Graph/BFS/boj_1926.py)
    - [백준 2178 - 미로탐색](https://www.acmicpc.net/problem/2178)
        - [풀이](/Algorithm/Graph/BFS/boj_2178.py)
    - [백준 7576 - 토마토](https://www.acmicpc.net/problem/7576)
        - [풀이](/Algorithm/Graph/BFS/boj_7576.py)
    - [백준 4179 - 불!](https://www.acmicpc.net/problem/4179)
    - [백준 1697 - 숨바꼭질 ](https://www.acmicpc.net/problem/1697)
- 심화