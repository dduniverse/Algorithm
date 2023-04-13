def solution(N, stages):
    fail = [0] * N # 실패율
    player = len(stages) # 스테이지별 유저 수
    for n in range(N):
        try:
            fail[n] = [n+1, stages.count(n+1) / player]
        except: # ZerodivisionError일 경우(=스테이지에 도달한 유저X) 실패율은 0
            fail[n] = [n+1, 0]
        player -= stages.count(n+1)
        
    return [i[0] for i in sorted(fail, key=lambda x:x[1], reverse=True)]
    