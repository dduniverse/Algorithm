import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 유저의 수, 친구 관계의 수

# 그래프 정보
D = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)] 

# 자기 자신 = 0
for i in range(1, n+1):
    D[i][i] = 0
    
# a, b는 서로 친구
for _ in range(m):
    a, b = map(int, input().split()) 
    D[a][b] = 1
    D[b][a] = 1

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                

# 케빈 베이컨의 수가 가장 작은 사람을 출력
min = sys.maxsize # 케빈 베이컨의 수
who = -1 # 유저 번호
for i in range(1, n+1):
    if min > sum(D[i][1:]):
        min = sum(D[i][1:])
        who = i

print(who)