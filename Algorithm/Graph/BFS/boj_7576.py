# 백준 2178 - 미로탐색
from collections import deque

#m 가로칸 n 세로칸
m, n = map(int,input().split())
tomato = []
queue = deque([])

# tomato [y][x]순으로 저장
for i in range(n):
    tomato.append(list(map(int,input().split())))

# 익은 토마도 위치 저장
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append((i,j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= m or ny < 0 or ny >= n: #tomato list out of range 방지
                continue
            if tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1
                queue.append((ny,nx))

bfs()
result = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))
print(result-1)