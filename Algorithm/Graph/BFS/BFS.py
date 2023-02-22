# BFS 구현
from collections import deque

class Graph:
    def __init__(self):
        self.list = {}

    def add_edge(self, u, v):
        if u not in self.list:
            self.list[u] = []
        if v not in self.list:
            self.list[v] = []
        self.list[u].append(v)
        self.list[v].append(u)

    def bfs(self, start):
        visited = set()

        queue = deque()

        visited.add(start)
        queue.append(start)

        while queue:

            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

graph.bfs(2)