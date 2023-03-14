# 재귀/Recursion
## [재귀 알고리즘이란 무엇일까?](./Recursion.md)
> 하나의 함수에서 반복적으로 스스로를 호출하여 작업을 수행하는 알고리즘   
- 함수를 명확하게 정의해야 한다.
- 모든 재귀 함수는 반복문으로도 동일한 동작할 수 있다.
    - 적재적소에 사용하면 코드가 간결해진다.
    - 메모리와 시간에서는 손해를 보게 된다.
- **절차적 사고가 아닌 재귀적 사고를 통해 생각하는것이 중요하다**

<br>

## 재귀함수의 조건
- 특정 입력에 대해서 자기 자신을 호출하지 않고 종료 되어야한다.
    - **Base case** 혹은 **base condition**이라고 함
    - 모든 입력은 base case로 수렴해야 한다.

## 장단점
- **장점**
    - 특정 유형의 문제를 해결하는 데 유용할 수 있다.

- **단점**
    - 많은 함수 호출과 메모리 사용을 요구하기 때문에 효율성이 더 떨어질 수 있다.


```Python
# 재귀 예시
def recursion(n):
    if n <= 0 : # Base case
        return 0
    return n + recursion(n-1) #Recursive case
print('Recursion result :',recursion(5))


res = 0
for i in range(5, 0, -1):
    res += i
print('for result :', res)
```

## 재귀 연습문제
- 기본
    - [백준 10872 - 팩토리얼](https://www.acmicpc.net/problem/10872)
        - [풀이](/Algorithm/Recursion/boj_10872.py)
    - [백준 1914 - 하노이 탑](https://www.acmicpc.net/problem/1914)
        - [풀이](/Algorithm/Recursion/boj_1914.py)
    - [백준 1629 - 곱셈](https://www.acmicpc.net/problem/1629)
        - [풀이](/Algorithm/Recursion/boj_1629.py)
- 심화