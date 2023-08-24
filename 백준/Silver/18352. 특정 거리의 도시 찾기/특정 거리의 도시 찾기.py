import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split()) # 도시개수, 도로개수, 거리정보, 출발도시

# 그래프 정보
graph = [[] for _ in range(n+1)]
for i in range(m):
    # A에서 B로 가는 도로 존재 = 1
    a, b = map(int, input().split())
    graph[a].append(b)


# BFS 함수
visited = [-1] * (n+1)   
def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] += 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            # 아직 방문하지 않은 인접노드라면
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
                

# BFS 함수 실행
bfs(x)

# 최단거리가 K인 도시
answer = [] 
for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

# 오름차순으로 정렬하여 출력
answer.sort()
if answer:
    for i in answer:
        print(i)
else:
    print(-1)