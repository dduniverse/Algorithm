def solution(today, terms, privacies):
    today = list(map(int, today.split('.'))) # [0]연, [1]월, [2]일
    terms = {i[0]: int(i[2:])for i in terms}
    
    answer = []
    for i, pri in enumerate(privacies):
        day, kind = pri.split()
        day = list(map(int, day.split('.')))
        month = terms[kind] # 유효기간
        
        day[1] += month
        while day[1] > 12:
            day[1] -= 12
            day[0] += 1
        
        day[2] -= 1        
        if day[2] == 0:
            day[2] = 28
            day[1] -= 1
        print(day)   
        
        if day[0] < today[0]:
            answer.append(i+1)
        elif day[0] == today[0] and day[1] < today[1]:
            answer.append(i+1)
        elif day[0] == today[0] and day[1] == today[1] and day[2] < today[2]:
            answer.append(i+1)
                    
    return answer
                    