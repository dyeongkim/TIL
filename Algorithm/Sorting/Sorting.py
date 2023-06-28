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
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        print("array is:", arr)
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 병합 정렬
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
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

# 퀵 정렬
def partition(arr, st, en):
    i = st - 1
    pivot = arr[en]

    for j in range(st, en):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[en] = arr[en], arr[i + 1]
    return i + 1

def quick_sort(arr, st, en):
    if len(arr) == 1:
        return arr
    if st < en:
        pi = partition(arr, st, en)
        quick_sort(arr, st, pi - 1)
        quick_sort(arr, pi + 1, en)

# 테스트 코드
arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort(arr,0, len(arr)-1)
print("Sorted array is:", arr)