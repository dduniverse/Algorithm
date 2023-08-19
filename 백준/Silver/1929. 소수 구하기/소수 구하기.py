import math

m, n = map(int, input().split())  # 범위
# 0부터 n까지의 배열
nums = [0, 0]
for i in range(2, n+1):
    nums.append(i)
    
for i in range(2, int(math.sqrt(n))+1):
    # 이미 지운 수는 다시 지우지 않음
    if nums[i] == 0: continue
    
    # i의 배수 제거(i는 지우지 않으므로 2배수부터 탐색)
    for j in range(i*2, n+1, i):
        nums[j] = 0

# m이상 n이하의 소수 출력        
for i in range(m, n+1):
    if nums[i] != 0:
        print(nums[i])