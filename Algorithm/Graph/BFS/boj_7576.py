# 백준 2178 - 미로탐색
from collections import deque

#m 가로칸 n 세로칸
m, n = map(int,input().split())
tomato = []

# tomato [y][x]순으로 저장
for i in range(n):
    tomato.append(list(map(int,input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))

    day = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= m or ny < 0 or ny >= n: #tomato list out of range 방지
                continue
            if tomato[ny][nx] == 0:
                tomato[ny][nx] = 2
                queue.append((ny,nx))
    
        day += 1

    return day

day_list = []

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            day_list.append(bfs(i,j))

print(max(day_list))
