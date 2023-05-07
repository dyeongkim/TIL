# 정렬/Sorting
> 어떤 데이터들이 주어졌을때 정해진 순서대로 나열하는 알고리즘

## 시간복잡도 O(N^2) 정렬
### 선택 정렬(Selection Sort)

![선택정렬](https://user-images.githubusercontent.com/113990279/236621593-daeed810-deb8-4b01-85bd-fdb284ff9d7a.gif)

(https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC:Selection-Sort-Animation.gif)

현재 위치에 들어갈 값을 찾아 정렬하는 알고리즘

1. 인덱스의 맨 앞부터 가장 작은 값을 찾아간다.
2. 가장 작은값을 찾으면 현재 인덱스 값과 바꾼다.
3. 다음 인덱스로 넘어가서 반복

```Python
# 선택정렬 예시
def selectSort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### 삽입 정렬(Insertion Sort)

![삽입정렬](https://user-images.githubusercontent.com/113990279/236684828-8f11e709-870a-44ef-b2a9-b0a4e946b454.gif)


(https://commons.wikimedia.org/wiki/File:Insertion-sort-example.gif)

1. 데이터를 하나씩 확인한다.
2. 배열에서 자신보다 작은 숫자를 찾는 순간 그 뒤에 삽입

```Python
# 삽입정렬 예시
def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else :
                break
```

### 버블 정렬(Bubble Sort)

![버블정렬](https://user-images.githubusercontent.com/113990279/236686661-6e489619-6036-43af-9736-cad882923f18.gif)

(https://commons.wikimedia.org/wiki/File:Bubble-sort-example-300px.gif)

1. 배열의 i번재 인덱스와 i+1번째 인덱스를 비교
2. i번째 인덱스가 더 크면 서로 교환(swap)
3. 반복

```Python
# 버블정렬 예시
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        print("array is:", arr)
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```


## 시간복잡도 O(NlogN) 정렬

### 벙합 정렬(Merge Sort)

```Python
# 병합정렬 예시
```

## 정렬 연습문제
- 기본
    - [백준 11728 - 배열합치기](https://www.acmicpc.net/problem/11728)
        - [풀이](/Algorithm/Sorting/boj_11728.py)