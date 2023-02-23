# 너비 우선 탐색/Breadth-first search(BFS)
> 노드에서 인접한 노드를 먼저 탐색하는 방법   
두 노드 사이의 최단경로 or 임의의 경로를 찾을 때 사용한다.   
구현할때 Queue를 사용   
인접한 노드를 Queue에 담고 하나씩 pop하며 다음 노드에서 다시 인접한 노드를 담는 식으로 구현한다.
<br>

## 장단점
- **장점**

- **단점**

## BFS 구현(Python)
```Python
# BFS 구현
from collections import deque

class Graph:
    def __init__(self):
        self.list = {}

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