import sys
input = sys.stdin.readline

k, n = map(int, input().split()) # 가지고 있는 랜선 k개, 필요한 랜선 n개
lines = [int(input()) for _ in range(k)] # k개의 랜선 길이

start, end = 1, max(lines)
answer = 0
while start <= end:
    mid = (start+end) // 2
    count = 0
    for line in lines:
        count += line // mid
        
    if count >= n:
        start = mid+1
        answer = max(answer, mid)
    else:
        end = mid-1
        
print(answer)