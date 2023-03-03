# 백준 2178 - 미로탐색
from collections import deque

n, m = map(int,input().split())
graph = []

# graph에 [y][x] 순서로 남음
for i in range(n):
    graph.append(list(input()))

# 방문한 칸 상 우 하 좌 좌표용 리스트
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):

    queue = deque()

    graph[y][x] = 0 # 방문한 경우 0으로 표시해서 재방문 방지
    queue.append((y,x))
    count = 1 # 그림 칸 개수초기화

    while queue:
        y,x = queue.popleft()
        for i in range(4): # dx, dy리스트를 이용해서 현재 좌표의 상 우 하 좌 
            ny = y + dy[i]
            nx = x + dx[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n: # 그림판 범위 밖으로 넘어가지 않게 조건문 설정 Out of range 방지
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((ny,nx))
                    count += 1
    return count

result = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result.append(bfs(i,j))

if len(result) == 0 : ## 결과가 없을때 max함수 valueError방지
    print(0)
    print(0)
else :
    print(len(result))
    print(max(result))