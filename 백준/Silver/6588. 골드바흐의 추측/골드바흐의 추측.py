import sys
import math

def is_Prime(n): # 소수 판별 함수
    if n==1: # 1은 소수가 아니므로 False
        return False
    for j in range(2,int(math.sqrt(n))+1): # n의 제곱근 이하의 수로 나누어 떨어지지 않으면 소수이다.
        if n%j==0: # 나누어 떨어지면 소수가 아니므로 False
            return False
    return True

while True:
    n=int(sys.stdin.readline().rstrip())
    if n==0: # 0을 입력하면 종료
        break
    
    flag=0 
    for a in range(3,n+1,2): # 3부터 n까지의 모든 수를 2씩 증가하며(홀수만 찾아야 하므로) 소수인지 체크함
        if is_Prime(a):
            if is_Prime(n-a): # a+b가 n이면 b는 n-a임을 활용하여 n-a가 소수인지 판별
                print(f'{n} = {a} + {n-a}')
                flag=1 # 가능하면 flag를 1로 바꿔줌
                break

    if flag==0: # 불가능할 시
        print('Glodbach\'s conjecture is wrong')