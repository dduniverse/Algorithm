m=int(input())
n=int(input())
lst=[]

for num in range(m,n+1): # m 이상 n 이하
    c=0 # 약수 개수를 세기 위한 c
    if num>1:
        for i in range(2,num): # 2 이상의 수로 나누어 떨어지면 그 수는 num의 약수
            if num%i==0:
                c=c+1 # 약수개수 +1
                break
        if c==0: # 약수개수가 0개 이면 = 소수이면
            lst.append(num)

if len(lst)==0:
    print(-1)
elif len(lst)>0:
    print(sum(lst))
    print(min(lst))