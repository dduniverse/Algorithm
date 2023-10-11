import sys

def solution(x, y, n):
    D = [sys.maxsize] * (y+1)   # DP 테이블
    D[x] = 0                    # 시작점
    
    for i in range(x, y+1):
        if D[i] == sys.maxsize:
            continue
        
        # 각 연산의 값이 범위(y)안에 있으면 min값으로 변경
        if i + n <= y:
            D[i+n] = min(D[i]+1, D[i+n])
        if i * 2 <= y:
            D[i*2] = min(D[i]+1, D[i*2])
        if i * 3 <= y:
            D[i*3] = min(D[i]+1, D[i*3])
    
    # x를 y로 만들 수 없으면 -1 리턴
    if D[y] == sys.maxsize:
        return -1
        
    return D[y]