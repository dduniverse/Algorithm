def solution(n, m, section):
    answer = 1
    paint = section[0]
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            paint = section[i]
            answer += 1
            
    return answer 