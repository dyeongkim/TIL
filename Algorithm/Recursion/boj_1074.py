# 백준 1074 - Z
'''
'''
def recursion(a, b):

N, r, c = map(int, input().split())

graph = [[-1] * N for _ in range(N)]