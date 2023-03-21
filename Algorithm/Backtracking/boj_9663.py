'''
isUsed1 : 세로 이동 체크
isUsed2 : 좌측하단에서 우측 상단 이동 체크
isUsed3 : 우측하단에서 좌측 상단 이동 체크
ex)
10000
00100
00000
00000
00000
으로 배치됐을때
Q k i
Q1 0,0
Q2 1,2
isUsed1 [T,F,T,F,F]
isUsed2 [T,F,F,T,F,F,F,F,F]
isUsed3 [F,F,F,T,T,F,F,F,F]
'''
N = int(input())
cnt = 0 #경우의 수
isUsed1, isUsed2, isUsed3 = [False]*40, [False]*40, [False]*40 #체스판 퀸 움직임 체크

def rec(k) : # 현재 배치될 행
    global cnt
    
    if k==N : # 끝까지 다 배치했으면 카운트
        cnt +=1
        return
    for i in range(N):
        if isUsed1[i] or isUsed2[i+k] or isUsed3[k-i+N-1] : # 세로, 대각선에 하나라도 겹치면 다음
            continue
        
        #안겹치면 배치
        isUsed1[i] = True
        isUsed2[i+k] = True
        isUsed3[k-i+N-1] = True
        # 다음 행
        rec(k+1)
        # 끝나면 다시 초기화
        isUsed1[i] = False
        isUsed2[i+k] = False
        isUsed3[k-i+N-1] = False

rec(0) # 0번째에서 시작
print(cnt)