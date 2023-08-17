from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split()) # n개의 수, 슬라이딩 윈도우 범위 l
nums = list(map(int, input().split()))

# n개의 (인덱스:값)을 저장하는 deque
numd = deque() 

for i in range(n):
    # deque에 있는 요소 중 슬라이딩 윈도우 범위를 벗어나면 삭제(맨 앞에 위치)
    if numd and numd[0][0] <= i - l:
        numd.popleft()
    
    # deque에 있는 요소 중 새로 들어오는 값보다 큰 값이 존재하면 삭제   
    while numd and nums[i] < numd[-1][1]:
        numd.pop()
    
    # deque에 (인덱스, 값) 추가    
    numd.append((i, nums[i]))
    
    # 최솟값 출력
    print(numd[0][1], end=' ')