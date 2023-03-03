# 백준 2178 - 미로탐색
from collections import deque

n, m = map(int,input().split())
graph = []

# graph에 [y][x] 순서로 남음
for i in range(n):
    graph.append(list(map(int,input())))

# 방문한 칸 상 우 하 좌 좌표용 리스트
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):

    queue = deque()
    queue.append((y,x))

    while queue:
        y,x = queue.popleft()
        for i in range(4): # dx, dy리스트를 이용해서 현재 좌표의 상 우 하 좌 
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: # 범위 밖으로 넘어가지 않게 Out of range 방지
                continue
            if graph[ny][nx] == 0: # 벽일경우 진행불가
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny,nx))
    return graph[n-1][m-1] # 마지막 칸이 출구니까 해당 번호가 이동거리

result = bfs(0,0)

print(result)