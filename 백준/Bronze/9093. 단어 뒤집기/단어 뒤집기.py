t=int(input())

for i in range(t):
    sentence=input().split()
    
    for s in sentence:
        print(s[::-1], end=' ')