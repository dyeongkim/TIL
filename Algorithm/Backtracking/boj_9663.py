N = int(input())
row = [0] * N
cnt = 0

def chk(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i ):
            return False        
    return True

def rec(k) :
    global cnt
    if k==N :
        cnt +=1
        return
    for i in range(N):
        row[k] = i
        if chk(k):
            rec(k+1)

rec(0)
print(cnt)