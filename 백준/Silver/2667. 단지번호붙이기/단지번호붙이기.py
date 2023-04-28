from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[x][y] = 0 # 다시 방문하지 않도록 값을 0으로 바꿈
    c = 1 # 집의 수(시작점도 같이 세야 하므로 1로 시작)

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or ny < 0 or nx >= n or ny >= n: # 범위를 벗어난 경우 무시
                continue
            if graph[nx][ny] == 1: # 집이 있으면 queue에 추가
                graph[nx][ny] = 0 # 다시 방문하지 않도록 값을 0으로 바꿈
                queue.append((nx, ny))
                c += 1 # 집의 수 +1
    return c

count = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(bfs(i ,j))

count.sort() # 오름차순 정렬
print(len(count)) # 단지의 개수 = count 길이
for i in count: # 오름차순으로 출력
    print(i)