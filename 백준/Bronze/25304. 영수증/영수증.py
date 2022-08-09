x=int(input())
n=int(input())

n_list=[]

for _ in range(n):
    a,b=map(int,input().split())
    n_list.append(a*b)

if sum(n_list)==x:
    print('Yes')
else:
    print('No')