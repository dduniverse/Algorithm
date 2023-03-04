def solution(emergency):
    answer = [0] * len(emergency)
    
    sort = sorted(emergency, reverse=True)
    
    for i in range(len(emergency)):
        for j in range(len(sort)):
            if emergency[i] == sort[j]:
                answer[i] = j + 1
                
    return answer