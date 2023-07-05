from collections import deque    
        
def solution(maps):
    n, m = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((0, 0)) # 시작 위치 큐에 추가
    
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # BFS
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny가 maps 범위 안에 있는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0: continue
                if maps[nx][ny] == 1: # 벽이 없으면 이동거리 +1, 새로운 위치 큐에 추가
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    else: # (n,m)으로 이동 불가하면(=제자리이면 1)
        return -1      