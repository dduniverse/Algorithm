import math

t=int(input())
for _ in range(t):
    n_list=list(map(int,input().split()))
    gcd=0
    for i in range(1,len(n_list)): # 0번 인덱스는 n_list의 요소 개수인 n이므로 1번부터 최대공약수를 찾는다
        for j in range(i+1,len(n_list)):
            gcd+=math.gcd(n_list[i],n_list[j]) # 모든 최대공약수의 합
    
    print(gcd)