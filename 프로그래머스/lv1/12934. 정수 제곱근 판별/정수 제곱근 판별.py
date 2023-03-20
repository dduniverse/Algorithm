def solution(n):
    sqrt = n**0.5
    if sqrt == int(sqrt):
        return (sqrt+1) ** 2
    return -1