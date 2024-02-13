from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # N개의 풍선
deq = deque(enumerate(map(int, input().split()))) # (인덱스, 값)으로 저장

answer = []

idx, rot = deq.popleft() # 첫 번째 풍선을 터트림
answer.append(idx+1) # 터진 풍선의 번호 기록

# queue에서 rotate는 양수일때 왼쪽으로, 음수일때 오른쪽으로 이동하므로 
# 문제에서 주어진 대로 양수일때 오른족으로 음수일때 왼족으로 이동하려면 앞에 -를 붙여줘야 함
while len(deq) > 0:
    if rot > 0:
        deq.rotate(-(rot-1))
    else:
        deq.rotate(-rot)

    idx, rot = deq.popleft()
    answer.append(idx+1) 

print(*answer)