# 탐욕 알고리즘/Greedy
> 현재 상황에서 지금 당장 좋은 것만 고르는 방법

## 설계 단계
1. 실현 가능성
2. 선택
3. 취소

## 예시
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