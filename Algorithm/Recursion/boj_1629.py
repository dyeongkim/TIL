# 백준 1629 - 곱셈
'''
시간 초과가 나오지 않게 재귀로 풀이
a^b를 a*a로 나눠서 해결
짝수면 a % C * a % c % c
홀수면 마지막에 a를 한번 더 곱해준다.
'''
def recursion(a, b):
    # base case
    if b <= 1 : # 1번이면 a%C
        return a % C
    tmp = recursion(a, b//2)
    if b % 2 == 0 :
        return tmp * tmp % C
    else:
        return tmp * tmp * a % C

    


A,B,C = map(int,input().split())

print(recursion(A, B))