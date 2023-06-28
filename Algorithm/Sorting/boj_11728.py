# 백준 11728 - 배열합치기
'''
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = A+B
result.sort()

print(*result)
'''
import sys

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j] :
                arr[k] = left[i]
                i += 1
            else :
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left) :
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right) :
            arr[k] = right[j]
            j += 1
            k += 1

input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

arr = A+B

merge_sort(arr)

print(*arr)

