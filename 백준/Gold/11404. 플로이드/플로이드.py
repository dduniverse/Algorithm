import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

# 최단 거리 리스트
D = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

# i == j이면 0으로 초기화
for i in range(1, n+1):
    D[i][i] = 0
    
# 그래프 정보
for i in range(m):
    a, b, c = map(int, input().split())
    if D[a][b] > c:
        D[a][b] = c # a에서 b로 가는 가중치 c

# 플로이드-워셜 알고리즘   
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])
            
# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if D[i][j] == sys.maxsize:
            D[i][j] = 0
            
for d in D[1:]:
    print(*d[1:])