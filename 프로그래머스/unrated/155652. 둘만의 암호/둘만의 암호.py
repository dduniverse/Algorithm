def solution(s, skip, index):
    answer = ''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alp = alp.replace(i, '')
    for i in s:
        idx = alp.index(i)
        answer += alp[(idx + index) % len(alp)]
    return answer