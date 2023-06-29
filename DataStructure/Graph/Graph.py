# 그래프 구현
# 무방향 그래프
class Undirected_Graph:
    def __init__(self):
        self.graph = {}
    
    # 노드 사이 간선(Egde) 연결
    def add_edge(self, u, v) :
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = [u]
        else:
            self.graph[v].append(u)

    def show_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print("Undirected_Graph Edge : node = ",node," Neighbour = ",neighbour)

# 방향 그래프
class Directed_Graph:
    def __init__(self):
        self.graph = {}
        
    # 노드 사이 간선(Egde) 연결
    def add_edge(self, u, v) :
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
    
    def show_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print("Directed_Graph Edge : node = ",node," Neighbour = ",neighbour)

# 그래프 생성
Dg = Directed_Graph()
Udg = Undirected_Graph()
# edge 추가
Dg.add_edge('A', 'B')
Dg.add_edge('B', 'C')
Dg.add_edge('A', 'C')
Dg.add_edge('D', 'C')

Udg.add_edge('A', 'B')
Udg.add_edge('B', 'C')
Udg.add_edge('A', 'C')
Udg.add_edge('D', 'C')

# Show edge
Dg.show_edges()
Udg.show_edges()