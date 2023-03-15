import math

def solution(a, b):
    gcd = math.gcd(a, b)
    b //= gcd
    
    num = []
    i = 2
    while i <= b:
        if b % i == 0:
            b //= i
            num.append(i)
        else:
            i += 1
    
    if all(i in [2,5] for i in num):
        return 1
    return 2
    