import sys
input = sys.stdin.readline

n, c = map(int, input().split()) # 집 N개, 공유기 C개
houses = [int(input()) for _ in range(n)] # 집의 좌표

houses.sort() # 이진 탐색을 수행할 배열 정렬

# 인접한 두 공유기 사이의 거리에 대한 이진 탐색
start, end = 1, houses[-1] - houses[0] # 최소=1, 최대=1번집~마지막집
max_len = 0

while start <= end:
    mid = (start + end) // 2 # 두 집 간 거리
    now = houses[0] # 현재 집 위치
    count = 1 # now에 공유기 한 개 설치

    # 현재집 위치+거리보다 더 멀리 위치한 집이면 공유기를 설치하고 해당 위치를 현재 집으로 변경
    for i in range(n):
        if houses[i] >= now + mid: 
            count += 1
            now = houses[i]
    
    if count >= c:
        max_len = max(max_len, mid) # 두 공유기 사이의 최대 거리 저장
        start = mid + 1
    else:
        end = mid -1

print(max_len)