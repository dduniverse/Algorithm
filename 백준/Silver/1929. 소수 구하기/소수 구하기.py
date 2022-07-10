import math

def yaksoo(n):
    if n==1: # 1은 약수가 아니므로 제외
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1): # n의 제곱근까지 약수가 존재하는지 확인(** 에라토스테네스의 체 참고)
            if n%i==0: # 약수가 존재하면 False
                return False
        return True # 존재하지 않으면 True

m,n=map(int,input().split())
for i in range(m,n+1):
    if yaksoo(i): # True이면 print 실행
        print(i)