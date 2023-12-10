import sys
input = sys.stdin.readline
n = int(input()) # 명령의 수

stack = []
for _ in range(n):
    command = input()

    if command[0] == '1':
        command, value = command.split()
        stack.append(int(value))
        
    elif command[0] == '2':
        if stack:
            top = stack.pop()
            print(top)
        else:
            print(-1)
            
    elif command[0] == '3':
        print(len(stack))
        
    elif command[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
            
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
