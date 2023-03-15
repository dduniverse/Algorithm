def solution(lines):
    answer = 0
    count = [0 for _ in range(200)] # -100 ~ 100 까지의 범위에서 해당 점에 선분이 그어진 횟수
    for line in lines:
        for i in range(line[0], line[1]): 
            count[i + 100] += 1
    answer += count.count(2) # 두 개 이상 겹친 점
    answer += count.count(3) # 세 개 이상 겹친 점
    return answer