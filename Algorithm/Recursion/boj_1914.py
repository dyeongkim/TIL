# 백준 1914 - 하노이타워
'''
base case
1개일때 1->3이동한다.

1. N-1개를 1에서 2로 옮겨놓는다.
2. 제일 밑을 3으로 옮긴다.
3. N-1개를 2에서 3으로 옮긴다
'''

def hanoi(N, f, b, t):
    if N <= 1: # base case
        print(f, t) # 1일때 1 -> 3 이동
        return 1
    
    hanoi(N-1, f, t, b) # N-1개를 1 -> 2 옮긴다.
    print(f, t)
    hanoi(N-1, b, f, t) # N-1개를 2 -> 3 옮긴다.
    

N = int(input())

print(2**N-1)
if ( N <= 20): # 20이하 일때만 출력
    hanoi(N, 1, 2, 3)
