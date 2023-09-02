import sys
input = sys.stdin.readline

n, k = map(int, input().split()) 

# DP 테이블
D = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    D[i][1] = i  # i개 중 1개를 뽑는 경우의 수 iC1 = i
    D[i][0] = 1  # i개 중 0개를 뽑는 경우의 수 iC0 = 1
    D[i][i] = 1  # i개 중 i개를 뽑는 경우의 수 iCi = 1

# 조합 점화식
for i in range(2, n+1):
    for j in range(1, i):  # j의 범위는 i보다 클 수 없음
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        
# nCk 출력
print((D[n][k]) % 10007)