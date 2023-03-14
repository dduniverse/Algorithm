def solution(sides):
    answer = []
    # 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
    
    for i in range(1, max(sides)+1): # sides에서 가장 큰 값이 가장 긴 변일 경우 
        if i + min(sides) > max(sides):
            answer.append(i)
    
    for i in range(max(sides)+1, sum(sides)): # 다른 한 변이 가장 긴 변일 경우 (<= sides 합)
        if i < sum(sides):
            answer.append(i)
    
    return len(answer)