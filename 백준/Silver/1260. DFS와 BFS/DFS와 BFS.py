from collections import deque

dfs_result = [] # dfs 결과 저장
def dfs(graph, v, visited):
    visited[v] = True # 방문했으면 True로 바꾸고 result에 저장
    dfs_result.append(v)
    for i in graph[v]: # 인접 노드 순차적으로 방문
        if not visited[i]:
            dfs(graph, i, visited)

bfs_result = []
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while(queue): # queue가 빌 때까지 반복
        v = queue.popleft() # queue에서 하나씩 가져오고, result에 추가
        bfs_result.append(v)

        for i in graph[v]: # 인접 노드 순차적으로 방문
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 번호
graph = [[] for _ in range(n+1)]

for i in range(1, m+1): # 연결된 노드 정보 추가
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1): # 오름차순으로 인접노드 방문하기 위해 정렬
    graph[i].sort()


visited = [False] * (n+1)
dfs(graph, v, visited)
print(*dfs_result)

visited = [False] * (n+1)
bfs(graph, v, visited)
print(*bfs_result)