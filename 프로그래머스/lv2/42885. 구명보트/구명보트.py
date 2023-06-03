def solution(people, limit):
    boat = 0
    people.sort() # 오름차순 정렬
    i, j = 0, len(people)-1 # 가벼운 사람, 무거운 사람
    while i <= j:
        if i == j: # 홀수명일 때 i, j가 같아짐 -> ex. [70, 80, 50]일 때 50 혼자 타야함
            boat += 1
            break
        elif people[i] + people[j] <= limit: # 무게 제한 이하이면 보트+1, 인덱스 +1, -1
            i += 1
            j -= 1
            boat += 1
        else: # 무게 제한 초과이면 무거운 사람 혼자 타게 보트+1, 덜 무거운 사람으로 바꿈
            j -= 1
            boat += 1
    return boat