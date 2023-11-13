from collections import deque

n = int(input()) # n장의 카드

queue = deque([i for i in range(1, n+1)])
for _ in range(n-1):
    queue.popleft() # 제일 위에 있는 카드를 버림
    queue.rotate(-1) # 남은 카드 중 제일 위에 있는 카드를 제일 밑으로 이동
    
print(queue[0])