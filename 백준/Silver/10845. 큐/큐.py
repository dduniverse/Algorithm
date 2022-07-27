import sys

n=int(sys.stdin.readline())
queue=[]

for i in range(n):
    command=sys.stdin.readline()

    if 'push' in command:
        queue.append(int(command.split()[1]))
    elif 'pop' in command:
        if len(queue)>0:
            num=queue.pop(0)
            print(num)
        else:
            print(-1)
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if len(queue)>0:
            print(0)
        else:
            print(1)
    elif 'front' in command:
        if len(queue)>0:
            print(queue[0])
        else:
            print(-1)
    elif 'back' in command:
        if len(queue)>0:
            print(queue[-1])
        else:
            print(-1)