from collections import deque

#R 행의 개수, C 열의 개수
r, c = map(int,input().split())
queue_J = deque()
queue_F = deque()

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

maze = []
for i in range(c):
	maze.append(list(input()))
	for j in range(r):
		if maze[i][j] == 'J':
			queue_J.append((0,i,j))
		elif maze[i][j] == 'F':
			queue_F.append((-1,i,j))

def bfs():
	while queue_J:
		jy, jx = queue_J.popleft()
		for i in range(4):
			jny = dy[i] + jy
			jnx = dx[i] + jx
			
			if maze[jny][jnx] == '#' or maze[jny][jnx] == 'F':
				continue
		
			if jnx >= r or jnx < 0 or jny >= c or jny < 0:
				return