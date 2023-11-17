import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split()) # 사람의 수, 친구 관계의 수

# 그래프 정보
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n # 방문 배열
answer = False # 주르륵 5명이 친구인 A-B-C-D-E가 존재하는지

# DFS 함수
def DFS(x, count):
    global answer
    
    # 5개가 되면 answer=True로 변경한 후 함수 종료
    if count == 5:
        answer = True
        return
    
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            DFS(i, count+1) # DFS 탐색 시 친구 수와 함께 넘겨줌
    
    visited[x] = False # 종료조건이 아니라면 다른 노드로부터 재탐색이 이뤄지므로 False로 바꿔줌

# 모든 노드에 대해 DFS를 수행
for i in range(n):
    DFS(i, 1)
    
    if answer:
        print(1)
        break
else:
    print(0)