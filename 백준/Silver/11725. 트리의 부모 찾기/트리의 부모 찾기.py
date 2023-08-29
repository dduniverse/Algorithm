import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

# 트리 정보 저장
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
parent = [0 for _ in range(n+1)] # 부모 노드
visited= [False for _ in range(n+1)] # 방문 여부

# DFS 함수
def DFS(x):
    visited[x] = True
    for t in tree[x]:
        if visited[t] == False:
            parent[t] = x
            DFS(t)

# 1번 노드부터 DFS 탐색           
DFS(1)

# 출력
print(*parent[2:])