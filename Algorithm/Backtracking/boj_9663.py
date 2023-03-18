N = int(input())
graph = [[False]*N for _ in range(N)]
cnt = 0


def rec(k) :
    if k==N :
        cnt +=1
        return

rec(4)
print(cnt)