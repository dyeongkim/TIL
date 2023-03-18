'''
주어진 숫자를 하나씩 사용하면서 모든 경우의 수를 계산
재귀를 통해 배열에 한칸씩 저장하여 길이 M을 모두 채우면 출력
'''
N, M = map(int,input().split())
arr = [-1]*10 # 수열을 저장하는 배열
used = [False]*10 # 해당 숫자가 사용됐는지 체크하기 위한 배열

def rec(k): # k개의 숫자가 할당됨
    if k==M: # M개만큼 저장됐으면 출력
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return
        
    
    for i in range(1,N+1): # k번째 칸에 1부터 N번까지 자연수를 대입하기 위한 반복문
        if not used[i]: # 자연수 i가 현재 수열에 사용됐는지 체크
            arr[k] = i # 사용 안됐으면 k번째 칸에 i 저장
            used[i] = True # i가 사용됨
            rec(k+1) # 다음칸에 저장하기위해 재귀
            used[i] = False # 재귀가 끝나면 i 미사용으로 돌려놓기
        

rec(0) #수열 시작은 0 개