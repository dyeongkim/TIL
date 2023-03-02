from collections import deque

def bfs(self,x,y):
    vis = set()
    queue = deque()

    vis.add((x,y))
    queue.append((x,y))
    count = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx

n, m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))


dx = [1,0,-1,0]
dy = [0,1,0,-1]
