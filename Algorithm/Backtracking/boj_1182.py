N, S = map(int,input().split())
val = list(map(int,input().split()))

def dfs(cur):
    if cur == N:
        return
    