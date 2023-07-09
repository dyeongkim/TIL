# 백트래킹/Backtracking
> 현재 상태에서 모든 후보군을 따라 들어가며 탐색하는 알고리즘 문제 해결 전략
- 가능한 모든 해결책이나 구성을 단계별로 검색
- 조건에 만족하지 않으면 되돌아가고 가지치기한다.
- **탐색 종료조건과 언제 가지치기 할 지가 중요**
<br>

## 백트래킹을 사용할 수 있는 문제
- 모든 경우의 수를 조사할 수 있을때
- 가능한 경우의 수가 많을때
- 가능한 해의 수가 유한할때

## 설계 단계
1. 문제 정의
2. 변수와 제약조건 정의
3. 반복   
   3.1. 경우의 수 생성   
   3.2. 생성한 경우의 수가 조건에 맞는지 체크
   3.3. 조건에 맞지 않으면 되돌아가기
4. 해를 찾거나 모든 수를 검사했는데도 찾지 못하면 종료

## BFS 연습문제
- 기본
    - [백준 15649 - N과 M](https://www.acmicpc.net/problem/15649)
        - [풀이](/Algorithm/Backtracking/boj_15649.py)
    - [백준 1182 -부분수열의 합](https://www.acmicpc.net/problem/1182)
        - [풀이](/Algorithm/Backtracking/boj_1182.py)
    - [백준 9663 - N-Queen](https://www.acmicpc.net/problem/9663)
        - [풀이](/Algorithm/Backtracking/boj_9663.py)
- 심화