# 정렬 알고리즘

# 선택 정렬
def select_sort(arr):
    for i in range(len(arr)-1):
        print("array is:", arr)
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 삽입 정렬
def insert_sort(arr):
    for i in range(1, len(arr)):
        print("array is:", arr)
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else :
                break
                

# 버블 정렬

# 병합 정렬
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

# 테스트 코드
arr = [64, 34, 25, 12, 22, 11, 90]
insert_sort(arr)
print("Sorted array is:", arr)