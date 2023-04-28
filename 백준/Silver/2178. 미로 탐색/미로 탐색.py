from collections import deque

n, m = map(int, input().split())

graph = [] # 2차원 리스트의 미로 정보
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    # 이동 방향(상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft() # 현재 좌표를 가져옴
        for i in range(4): # 상하좌우로 이동한 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 공간을 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0: # 이동할 수 없는 칸이면 무시 
                continue
            if graph[nx][ny] == 1: # 처음 방문한 노드이면 해당 좌표 값 +1(= 방문했다는 표시)
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) # queue에 이동한 좌표 추가
    
    return graph[n-1][m-1] # (n, m)까지의 최단 거리 반환

print(bfs(0, 0))