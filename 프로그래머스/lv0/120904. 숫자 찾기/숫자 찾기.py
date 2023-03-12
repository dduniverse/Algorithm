def solution(num, k):
    answer = 0
    index = str(num).find(str(k))
    if index >= 0:
        answer = index + 1
    else:
        answer = index
    return answer