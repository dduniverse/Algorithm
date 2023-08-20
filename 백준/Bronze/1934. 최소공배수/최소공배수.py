t = int(input()) # 테스트 케이스의 개수
for i in range(t):
    a, b = map(int, input().split())
    
    ab = a * b
    
    # 최대 공약수 구하기(유클리드 호제법)
    while a % b > 0:
        a, b = b, a % b   
    gcd = b
    
    # 최소 공배수 = a*b / gcd
    lcm = ab // gcd
    print(lcm)