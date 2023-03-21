L, C = map(int,input().split())
alpha = list(map(int(input().split())))

alpha.sort()

def recur(cur) :
    if cur == L : 
        