n=int(input())

for i in range(n):
    score=0
    sum=0

    result=input()
    
    for i in result:
        if i=='O':
            score+=1
            sum=sum+score
        elif i=='X':
            score=0
    print(sum)