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