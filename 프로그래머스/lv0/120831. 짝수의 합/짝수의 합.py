def solution(n):
    answer = 0
    
    num = [i for i in range(1, n+1) if i % 2==0]
    
    answer = sum(num)
    
    return answer