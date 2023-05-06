# 정렬/Sorting
> 어떤 데이터들이 주어졌을때 정해진 순서대로 나열하는 알고리즘

## 시간복잡도 O(N^2) 정렬
### 선택 정렬(Selection Sort)

![선택정렬](https://user-images.githubusercontent.com/113990279/236621593-daeed810-deb8-4b01-85bd-fdb284ff9d7a.gif)

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

- 삽입 정렬(Insertion Sort)
- 버블 정렬(Bubble Sort)

## 시간복잡도 O(NlogN) 정렬

### 벙합 정렬(Merge Sort)

```Python
# 병합정렬 예시
```

## 정렬 연습문제
- 기본
    - [백준 11728 - 배열합치기](https://www.acmicpc.net/problem/11728)
        - [풀이](/Algorithm/Sorting/boj_11728.py)