def solution(spell, dic):
    answer = 2
    for d in dic:
        flag = 0
        for s in spell:
            if s in d:
                flag += 1
        if flag == len(spell):
            answer = 1
    return answer
            
