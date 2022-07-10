import math

def sosu(n):
    if n==1: # 1은 소수가 아니므로 제외
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1): # n의 제곱근까지 약수가 존재하는지 확인(** 에라토스테네스의 체 참고)
            if n%i==0: # 약수가 존재하면 False
                return False
        return True # 존재하지 않으면 True

lim=list(range(2,246912)) # 제한된 범위
lim_sosu=[] # 제한된 범위 안에서의 소수 리스트
for i in lim:
    if sosu(i):
        lim_sosu.append(i)

while True:
    n=int(input())
    c=0
    if n==0:
        break

    for i in lim_sosu:
        if n<i<=2*n: # 제한된 범위 안에서의 소수 리스트 중 n에서 2n까지의 소수의 개수
            c=c+1
    print(c)