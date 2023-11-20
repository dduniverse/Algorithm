import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색 시작 정점 번호

# 그래프 정보
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

# 방문 정보
d_visited = [False for _ in range(n+1)]
b_visited = [False for _ in range(n+1)]

# DFS 함수
def DFS(x):
    d_visited[x] = True
    print(x, end=' ')
    
    for i in graph[x]:
        if not d_visited[i]:
            DFS(i)

# BFS 함수 
def BFS(x):
    queue = deque()
    queue.append(x)
    
    b_visited[x] = True
    
    while queue:
        n = queue.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not b_visited[i]:
                b_visited[i] = True
                queue.append(i)

# 출력
DFS(v)
print()           
BFS(v)