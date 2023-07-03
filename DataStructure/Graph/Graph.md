# 그래프(Graph)
> 연결할 객체를 나타내는 정점(Vertex)와 간선(Edge)로 구성된 한정된 자료구조

- 그래프는 개체 간의 관계를 나타내는데 탁월하다.
- 개체 간의 관계가 중요한 개체 집합이 있을때 사용된다.
    - ex) 네트워크, 웹 페이지, 종속 트리

<br>

## 장단점
- **장점**
    - 관계 표현
        - 개체 간의 복잡한 관계를 나타내는데 탁월.
        - 네트워크, 데이터 구성, 계산 장치, 계산 흐름 등을 나타내는데 사용
    - 경로 찾기
        - 두 노드 사이의 최단 경로를 찾는데 유용

- **단점**
    - 저장공간
        - 각 node와 edge를 저장해야 하므로 메모리가 많이 소모됨


### 그래프 구현(Python)
```Python
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
```
