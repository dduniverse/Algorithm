c = 0 # 바이러스에 감염된 컴퓨터의 수
def dfs(graph, v, visited):
    visited[v] = True
    global c 
    c += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결된 컴퓨터의 쌍

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

dfs(graph, 1, visited)
print(c-1) # 1번을 통해 감염되는 수를 구해야 하므로 1번을 제외한 감염된 컴퓨터의 수