N, S = map(int,input().split()) #정수 N개 합 S
val = list(map(int,input().split())) # 수열
cnt = 0 # 개수
arr_sum = 0 # 수열 합

def dfs(cur):
    global cnt, arr_sum

    # 마지막이면 리턴
    if cur == N:
        return
    
    #합이 S면 카운트
    if S == arr_sum + val[cur]:
        cnt += 1

    #이번원소를 포함하지 않고 다음 수
    dfs(cur+1)

    # 이번원소를 포함하고 시도
    arr_sum += val[cur]
    dfs(cur+1)

    # 마지막에 다시 이번 원소를 빼 줘야함
    arr_sum -= val[cur]


dfs(0)

print(cnt)