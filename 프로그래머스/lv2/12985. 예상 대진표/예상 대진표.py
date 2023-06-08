def solution(n,a,b):
    a, b = min(a, b), max(a, b)
    round = 0
    while a != b:
        round += 1
        if a % 2 == 0:
            a = a // 2
        else:
            a = a // 2 + 1
        
        if b % 2 == 0:
            b = b // 2
        else:
            b = b // 2 + 1
            
    return round