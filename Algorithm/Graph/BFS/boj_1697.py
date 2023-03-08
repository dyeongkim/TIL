from collections import deque

graph = [-1]*100001
N, K = map(int,input().split())
graph[N], graph[K] = 0, -2

queue = deque()
queue.append(N)

def bfs():
	while queue:
		n = queue.popleft()

		for i in [n+1, n-1, 2*n] :
			if i < 0 or i >= 100001:
				continue

			if graph[i] == -2:
				return graph[n]+1
			
			if graph[i] == -1 :
				graph[i] = graph[n]+1
				queue.append(i)

print(bfs())