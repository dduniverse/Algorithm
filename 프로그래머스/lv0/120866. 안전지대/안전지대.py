import numpy as np

def solution(board):
    n = len(board)
    map = [[0]*(len(board)+2) for _ in range(len(board)+2)] # n+2 * n+2 행렬
    map = np.array(map)

    bomb = [] # 지뢰 위치 저장
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb.append((i+1, j+1)) # map 기준 지뢰 위치
                map[i+1][j+1] = 1 # map에서 지뢰 표시
    #print(board)
    #print(map)
    #print(bomb)

    for i,j in bomb: # 지뢰 주변 지역
        map[i+1][j] = 1
        map[i-1][j] = 1
        map[i][j+1] = 1
        map[i][j-1] = 1
        map[i+1][j+1] = 1
        map[i+1][j-1] = 1
        map[i-1][j+1] = 1
        map[i-1][j-1] = 1
    #print(map)
    map = map[1:n+1,1:n+1] # board와 같은 크기로 슬라이싱
    #print(map)
    answer = n*n - np.sum(map) # 전체 칸 수 - 1의 개수(= 1을 다 더한 값)
    return int(answer)