import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(n):
    answer = 0
    piece = lcm(6, n)
    answer = piece / 6
    return answer