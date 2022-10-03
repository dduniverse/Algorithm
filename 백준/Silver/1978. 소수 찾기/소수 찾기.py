n=int(input())
number=list(map(int,input().split()))

for num in number:
    if num==1: # 입력된 수에 1이 있으면 n-1
        n=n-1
    
    for i in range(2,num): # 2이상의 수로 나누어 떨어지면 n-1 을 해준다.
        if num%i==0: 
            n=n-1 
            break # 2로 나누어 떨어지는 수가 4로도 나누어 떨어지면 -1이 2번되므로 한번만 -1하기 위해 break를 작성해줌

print(n)