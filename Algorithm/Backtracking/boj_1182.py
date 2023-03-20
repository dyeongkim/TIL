N, S = map(int,input().split())
val = list(map(int,input().split()))
cnt = 0
arr_sum = 0

def dfs(cur):
    global cnt, arr_sum

    if cur == N:
        return
    
    if S == arr_sum + val[cur]:
        cnt += 1

    dfs(cur+1)

    arr_sum += val[cur]
    dfs(cur+1)

    arr_sum -= val[cur]


dfs(0)

print(cnt)