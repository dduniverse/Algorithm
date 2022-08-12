import sys

t = int(sys.stdin.readline())
prime = [True for i in range(1000001)] # 전체 리스트를 만들고 확인하는 방식이 시간초과를 피할 수 있음
prime[0] = prime[1] = False # 0과 1은 소수가 아니므로 False

for i in range(2, 1001): # 1001은 1000000의 제곱근이므로 1001까지만 확인하면 시간이 줄어듦 => 에라토스테네스의 체 활용
    for j in range(i*2, 1000001, i): # i의 배수는 소수가 아니므로 False로 바꿔줌
        prime[j] = False

for i in range(t):
    c = 0
    n = int(sys.stdin.readline())

    for a in range(2,n//2+1): # 2부터 하나씩 차례로 소수인지 판별
        if prime[a] and prime[n-a]: # n=a+b이면 b는 n-a임을 활용하여 모두 소수이면 c+1
            c += 1 
    print(c)