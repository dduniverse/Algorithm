def solution(s):
    answer = ''
    for i in set(s):
        if s.count(i) == 1:
            answer += i
    answer = ''.join(sorted(answer))
    return answer