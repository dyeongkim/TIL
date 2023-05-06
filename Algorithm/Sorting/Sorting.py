# 정렬 알고리즘

# 선택 정렬
def selectSort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 삽입 정렬

# 버블 정렬

# 병합 정렬
def mergeSort(arr):
    if len(arr)