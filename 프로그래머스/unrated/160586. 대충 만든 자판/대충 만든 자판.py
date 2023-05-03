def solution(keymap, targets):
    answer = []
    km = {}
    for key in keymap:
        for i, k in enumerate(key):
            km[k] = min(i+1, km[k]) if k in km else i+1
    print(km)
    
    for i, target in enumerate(targets):
        c = 0
        for t in target:
            if t not in km:
                answer.append(-1)
                break
            c += km[t]
        else:
            answer.append(c)
    
    return answer