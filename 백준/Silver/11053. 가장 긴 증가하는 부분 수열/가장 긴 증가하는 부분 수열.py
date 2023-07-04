n = int(input()) # 수열의 쿠기
array = list(map(int, input().split())) # 수열

dp = [1] * n # DP 테이블(array[i]를 마지막 원소로 하는 수열의 최대 길이)

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]: # 뒤 요소(i)가 항상 앞 요소(i)보다 커야함
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))