import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 강의 수, 블루레이 수
time = list(map(int, input().split())) # 강의 길이

answer = 10000
start, end = max(time), sum(time)
while start <= end:
    mid = (start + end) // 2 
    total = 0
    count = 0
    for i in range(n):
        if total + time[i] > mid:    # 현재 블루레이에 추가할 수 없으면
            count += 1               # 블루레이 개수 +1
            total = 0                # 새로운 블루레이 시간 0으로 초기화
        total += time[i]             # 블루레이에 새로운 강의 영상 추가

    if total > 0:                    # 남은 영상이 있으면 블루레이 개수 +1
        count += 1
    
    if count > m:
        start = mid+1
    else:
        end = mid-1
        answer = mid

print(answer)