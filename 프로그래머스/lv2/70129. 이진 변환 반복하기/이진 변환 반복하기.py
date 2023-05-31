def solution(s):
    turn, o = 0, 0 # 회차, 제거한 0의 개수
    
    # 1이 될 때까지 반복
    while int(s) != 1: 
        zero = s.count('0') # 0의 개수
        c = len(s) - zero # 0 제거 후 길이
        s = bin(c)[2:] # 이진 변환 결과
        
        o += zero
        turn += 1
        
    return [turn, o]