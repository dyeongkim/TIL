import sys
from collections import deque

#R 행의 개수, C 열의 개수
r, c = map(int,input().split())
queue_J, queue_F = deque(), deque()
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
maze = [list(input().strip()) for i in range(r)]

#방문정보를 -1로 초기화
dist_j, dist_f = [[-1]*c for i in range(r)], [[-1]*c for i in range(r)] # -1을 c만큼 반복한 배열을 r만큼 반복 [r][c]

for i in range(r):
	for j in range(c):
		if maze[i][j] == 'J': # 큐에 J 위치 담고 시작, 방문정보에 시작점 설정
			queue_J.append((i,j))
			dist_j[i][j] = 0
		elif maze[i][j] == 'F':# 큐에 F 위치 담고 시작, 방문정보에 시작점 설정
			queue_F.append((i,j))
			dist_f[i][j] = 0

def bfs():

	# F부터 BFS 실행
	while queue_F:
		fx, fy = queue_F.popleft()
		for i in range(4):
			ny = dy[i] + fy
			nx = dx[i] + fx
			
			if nx < 0 or nx >= r or ny < 0 or ny >= c :#불은 범위 밖으로 안나가도록
				continue
			if dist_f[nx][ny] >= 0 or maze[nx][ny] == '#':# -1 이상이면 방문했던 칸, #은 벽
				continue
			dist_f[nx][ny] = dist_f[fx][fy]+1
			queue_F.append((nx,ny))

	# J에 대한 BFS실행
	while queue_J:
		jx, jy = queue_J.popleft()
		for i in range(4):
			ny = dy[i] + jy
			nx = dx[i] + jx
			# 지훈이는 범위 밖으로 나가면 탈출로 간주
			if nx < 0 or nx >= r or ny < 0 or ny >= c :
				return dist_j[jx][jy] + 1 #현재 위치에 +1해서 탈출까지 걸린시간 체크
			if dist_j[nx][ny] >= 0 or maze[nx][ny] == '#': # -1 이상이면 방문했던 칸, #은 벽
				continue
			if dist_f[nx][ny] != -1 and dist_f[nx][ny] <= dist_j[jx][jy]+1: # 다음 도착한 위치에 불이 방문했는지 체크 and 해당 칸 불 도착시간 <= 내가 도착한 시간 (내가 늦게 도착했다는 뜻)
				continue
			dist_j[nx][ny] = dist_j[jx][jy]+1
			queue_J.append((nx,ny))
	return 0

	
res = bfs()
if res != 0:
	print(res)
else:
	print('IMPOSSIBLE')