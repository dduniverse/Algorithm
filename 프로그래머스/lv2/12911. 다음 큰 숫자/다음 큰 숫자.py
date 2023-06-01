def solution(n):
    n_1 = bin(n)[2:].count('1') # 2진수로 변환했을 때 1의 개수
    for i in range(n+1, 1000000): # n보다 큰 자연수 중에서
        next_1 = bin(i)[2:].count('1') # 2진수로 변환했을 때 1의 개수가 같으면 return
        if n_1 == next_1:
            return i