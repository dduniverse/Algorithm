import sys
input = sys.stdin.readline

n = int(input()) # 지방의 수
budget = list(map(int, input().split())) # 각 지방의 예산요청
m = int(input()) # 총 예산

start, end = 0, max(budget)
answer = 0
while start <= end:
    mid = (start+end) // 2 # 상한액
    total = 0
    for i in range(n):
        if budget[i] >= mid:
            total += mid
        else:
            total += budget[i]
            
    if total > m:
        end = mid-1
    else:
        start = mid+1
        answer = max(answer, mid)
        
        
print(answer)
