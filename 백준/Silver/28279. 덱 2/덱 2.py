from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 명령의 수
deq = deque()

for _ in range(n):
    command = input()

    if command.startswith('1'):
        _, x = command.split()
        deq.appendleft(x)       # 덱의 앞에 x 추가
    elif command.startswith('2'):
        _, x = command.split()
        deq.append(x)           # 덱의 뒤에 x 추가
    elif command.startswith('3'):
        if len(deq) > 0:
            print(deq.popleft()) # 정수가 존재하면 맨 앞의 값 빼고 출력
        else:
            print(-1)
    elif command.startswith('4'):
        if len(deq) > 0:
            print(deq.pop())    # 정수가 존재하면 맨 뒤의 값 빼고 출력
        else:
            print(-1)
    elif command.startswith('5'):
        print(len(deq))         # 덱의 길이 출력
    elif command.startswith('6'):
        if len(deq) == 0:       # 덱이 비어있으면 1 아니면 0
            print(1)
        else:
            print(0)
    elif command.startswith('7'):
        if len(deq) > 0:
            print(deq[0])       # 정수가 존재하면 맨 앞 정수 출력
        else:
            print(-1)
    elif command.startswith('8'):
        if len(deq) > 0:        # 정수가 존재하면 맨 뒤 정수 출력
            print(deq[-1])
        else:
            print(-1)