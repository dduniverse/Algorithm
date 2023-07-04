n = int(input()) # n개의 정수
array = list(map(int, input().split())) # n개의 정수로 이루어진 수열

# DP 테이블
dp = [0] * n
dp[0] = array[0]
for i in range(1, n):
    dp[i] = max(array[i], dp[i-1] + array[i])

print(max(dp))