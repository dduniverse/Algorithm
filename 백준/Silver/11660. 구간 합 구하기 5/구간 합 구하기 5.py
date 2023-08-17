import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 표의 크기, 합을 구해야 하는 횟수

A = [] # NxN 리스트
for _ in range(n):
    A.append(list(map(int, input().split())))
    
dp = [[0]*(n+1) for i in range(n+1)] # DP 테이블

# 합 배열 D 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + A[i-1][j-1] # 구간 합

# x1,y1에서 x2,y2까지의 합        
for k in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1])