import math

def is_Prime(n): # 소수 판별 함수
    if n==1: # 1은 소수가 아니므로 False
        return False
    for j in range(2,int(math.sqrt(n))+1): # n의 제곱근 이하의 수로 나누어 떨어지지 않으면 소수이다.
        if n%j==0: # 나누어 떨어지면 소수가 아니므로 False
            return False
    return True

t=int(input()) # 테스트 케이스 개수 T
for i in range(t):
    n=int(input()) # 테스트할 짝수 n 입력
    a=b=n//2
    while a>0:
        if is_Prime(a) and is_Prime(b): # a와 b 모두 소수이면 출력
            print(a,b)
            break
        else: # 둘 중 하나라도 아니라면 각각 -1, +1씩 해보면서 두 수가 모두 소수인지 확인
            a-=1
            b+=1