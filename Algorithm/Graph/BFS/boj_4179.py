from collections import deque

#R 행의 개수, C 열의 개수
r, c = map(int,input().split())
queue_J = deque()
queue_F = deque()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

maze = []
dist_j = []
dist_f = []

res = 0
for i in range(c):
	maze.append(list(input()))
	dist_j.append([])
	dist_f.append([])
	for j in range(r):
		dist_j[i].append(-1)
		dist_f[i].append(-1)
		if maze[i][j] == 'J':
			queue_J.append((i,j))
			dist_j[i][j] = 0
		elif maze[i][j] == 'F':
			queue_F.append((i,j))
			dist_f[i][j] = 0

def bfs():
	while queue_F:
		fy, fx = queue_F.popleft()
		for i in range(4):
			ny = dy[i] + fy
			nx = dx[i] + fx
			if nx < 0 or nx >= r or ny < 0 or ny >= c :
				continue
			if dist_f[ny][nx] >= 0 or maze[ny][nx] == '#':
				continue
			dist_f[ny][nx] = dist_f[fy][fx]+1
			queue_F.append((ny,nx))
	while queue_J:
		jy, jx = queue_J.popleft()
		for i in range(4):
			ny = dy[i] + jy
			nx = dx[i] + jx
			if nx < 0 or nx >= r or ny < 0 or ny >= c :
				return dist_j[jy][jx] + 1
			if dist_j[ny][nx] >= 0 or maze[ny][nx] == '#':
				continue
			if dist_f[ny][nx] != -1 and dist_f[ny][nx] <= dist_j[jy][jx]+1:
				continue
			dist_j[ny][nx] = dist_j[jy][jx]+1
			queue_J.append((ny,nx))
	return 0

	
res = bfs()
if res != 0:
	print(res)
else:
	print('IMPOSSIBLE')