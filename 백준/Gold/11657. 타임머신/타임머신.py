import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 에지 리스트
edge = []
for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))

# 정답 리스트    
D = [sys.maxsize] * (n+1)
D[1] = 0

# 벨만-포드 알고리즘즘
for _ in range(n-1):
    for s, e, w in edge:
        if D[s] != sys.maxsize and D[e] > D[s] + w:
            D[e] = D[s] + w

# 사이클 존재 여부 확인
cycle =  False         
for s, e, w in edge:
    if D[s] != sys.maxsize and D[e] > D[s] + w:
            cycle = True

# 사이클이 존재하면 -1 출력            
if cycle:
    print(-1)
# 사이클이 존재하지 않으면
else:
    # 1번 노드에서 i번 노드로 가는 최단 경로 출력(i >= 2)
    for i in range(2, n+1):
        if D[i] == sys.maxsize:
            print(-1)
        else:
            print(D[i])