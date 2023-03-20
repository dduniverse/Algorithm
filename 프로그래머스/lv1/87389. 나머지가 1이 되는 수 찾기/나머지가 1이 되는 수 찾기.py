def solution(n):
    i = 2
    while i < n:
        if (n-1) % i == 0:
            return i
            break
        i += 1
