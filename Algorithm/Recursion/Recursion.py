# 재귀 예시
def recursion(n):
    if n <= 0 : # Base case
        return 0
    return n + recursion(n-1)

print('Recursion result :',recursion(5))



res = 0
for i in range(5, 0, -1):
    res += i

print('for result :', res)