def solution(brown, yellow):
    for i in range(int(yellow ** 0.5), 0, -1):
        if yellow % i == 0 and ((yellow // i)+2) * (i+2) == brown + yellow:
            return [(yellow // i)+2, i+2]