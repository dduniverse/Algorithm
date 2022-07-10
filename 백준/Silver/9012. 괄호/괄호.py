n=int(input())
for i in range(n):
    str=input()
    c=0

    for s in str:
        if s=='(':
            c=c+1
        elif s==')':
            c=c-1
        if c<0: # 여는 괄호 없이 닫는 괄호가 왔을 때
            print('NO')
            break
    
    if c==0:
        print('YES')
    elif c>0:
        print('NO')