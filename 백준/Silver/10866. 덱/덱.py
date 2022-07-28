import sys

n=int(sys.stdin.readline())
deck=[]

for i in range(n):
    command=sys.stdin.readline().split()

    if command[0]=='push_front':
        deck.insert(0, int(command[1]))
    if command[0]=='push_back':
        deck.append(int(command[1]))
    if command[0]=='pop_front':
        if len(deck)>0:
            print(deck.pop(0))
        else:
            print(-1)
    if command[0]=='pop_back':
        if len(deck)>0:
            print(deck.pop(-1))
        else:
            print(-1)
    if command[0]=='size':
        print(len(deck))
    if command[0]=='empty':
        if len(deck)>0:
            print(0)
        else:
            print(1)
    if command[0]=='front':
        if len(deck)>0:
            print(deck[0])
        else:
            print(-1)
    if command[0]=='back':
        if len(deck)>0:
            print(deck[-1])
        else:
            print(-1)