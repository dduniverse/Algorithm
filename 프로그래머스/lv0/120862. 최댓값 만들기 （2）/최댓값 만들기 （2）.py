from itertools import combinations 

def solution(numbers):
    com = list(combinations(numbers, 2))
    return max([i[0]*i[1] for i in com])