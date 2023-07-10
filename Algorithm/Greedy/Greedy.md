# 탐욕 알고리즘/Greedy
> 현재 상황에서 지금 당장 좋은 것만 고르는 방법

## 원리
- 각 단계에서 가장 좋아 보이는 선택을 한 다음 발생하는 하위 문제를 해결하는것
- 더 큰 그림이나 선택의 결과를 고려하지 않음.

## 설계 단계
1. 실현 가능성
2. 선택
3. 취소

## 예시1
### 동전 문제

거슬러줄 수 있는 잔돈이 10,50,100,500 N원 받았을때 잔돈 개수를 구하시오

```Python
N = 1280
coin=[10,50,100,500]
coin=sorted(coin,reverse=True)
print(coin)

for i in coin:
    print('%s원 %s개'%(i,N//i))
    N=N%i
```
## 예시2
### 활동 선택 문제

시작 및 종료 시간과 함께 n 활동이 제공됩니다.   
한 사람이 한 번에 하나의 활동만 수행할 수 있다고 가정하고 한 사람이 수행할 수 있는 최대 활동 수를 선택하시오.

```Python
activities = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]
activities.sort(key = lambda x: x[1])

print(activities[0])

i = 0
for j in range(1, len(activities)):
    if activities[j][0] >= activities[i][1]:
        print(activities[j])
        i = j
```