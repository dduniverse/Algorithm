import sys

n=int(sys.stdin.readline())
stack=[]

for i in range(n):
    command=sys.stdin.readline()
    
    if 'push' in command:
        stack.append(int(command.split()[1]))
    
    if 'pop' in command:
        if len(stack)>=1:
            s_pop=stack.pop()
            print(s_pop)
        else:
            print(-1)
    
    if 'size' in command:
        print(len(stack))
    
    if 'empty' in command:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if 'top' in command:
        if len(stack)>=1:
            print(stack[-1])
        else:
            print(-1)