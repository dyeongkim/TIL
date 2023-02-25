# 깊이 우선 탐색/Depth-First Search(DFS)
> 다음 노드로 접근하기 전에 노드의 모든 자식 노드를 방문하는 알고리즘   
<br>

## 장단점
- **장점**
    - BFS에 비해서 메모리를 덜 사용한다.
    - BFS에 비해서 구현이 쉽다.

- **단점**
    - DFS의 경로가 최단 경로는 아니다.

## BFS 구현(Python)


```Python
# DFS구현
class Graph:
    def __init__(self):
        self.list = {}

    def add_edge(self, u, v):
        if u not in self.list:
            self.list[u] = []
        self.list[u].append(v)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        if v in self.list :
            for neighbor in self.list[v]:
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()

        self.dfs_util(start,visited)
        

graph = Graph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)

graph.dfs(0)
```