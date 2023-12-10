from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 연산의 개수
queue = deque()

for _ in range(n):
    command = input()
    
    if command.startswith('push'):
        _, value = command.split()
        queue.append(int(value))
    elif command.startswith('pop'):
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command.startswith('size'):
        print(len(queue))
    elif command.startswith('empty'):
        if queue:
            print(0)
        else:
            print(1)
    elif command.startswith('front'):
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command.startswith('back'):
        if queue:
            print(queue[-1])
        else:
            print(-1)