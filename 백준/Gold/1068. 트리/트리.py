import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 트리의 노드 개수
p = list(map(int, input().split())) # 부모 정보

# 트리 정보
tree = [[] for _ in range(n)] 
for i in range(n):
    # 부모가 없다면(-1) 루트 노드
    if p[i] == -1:
        root= i
    else:
        tree[i].append(p[i])
        tree[p[i]].append(i)
        
d_node = int(input()) # 삭제 노드

leaf = 0  # 리프 노드 수
visited = [False for _ in range(n)] # 방문 배열

# DFS 함수
def DFS(x):
    global leaf
    child = 0  # 자식 수
    visited[x] = True
    
    for i in tree[x]:
        # 방문하지 않은 노드이면서 삭제 노드가 아니면 자식 수 +1, DFS 실행
        if not visited[i] and i != d_node:
            child += 1
            DFS(i)
            
    # 자식 수 = 0이면 리프 노드
    if child == 0:
        leaf += 1

# 삭제 노드 = 루트 노드이면 모든 노드가 지워지므로 리프노드 0개
if d_node == root:
    print(0)
else:
    DFS(root)
    print(leaf)