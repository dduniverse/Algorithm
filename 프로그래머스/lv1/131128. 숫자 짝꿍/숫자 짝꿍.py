from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    
    answer = ''
    for i in range(10):
        answer += str(i) * (min(x[str(i)], y[str(i)]))
    
    if answer == '':
        return '-1'
    
    answer = ''.join(sorted(answer, reverse=True))
    if answer[0] == '0':
        return '0'
    else:
        return answer