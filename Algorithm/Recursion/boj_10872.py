# 백준 10872 - 팩토리얼
def factorial(n):
    if n <= 0 : # base case
        return 1
    return n * factorial(n-1)

N = int(input())
print(factorial(N))