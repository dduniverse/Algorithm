def solution(people, limit):
    boat = 0
    people.sort() # 오름차순 정렬
    i, j = 0, len(people)-1 # 0번 인덱스, 마지막 인덱스
    while i <= j:
        if i == j:
            boat += 1
            break
        elif people[i] + people[j] <= limit:
            i += 1
            j -= 1
            boat += 1
        else:
            j -= 1
            boat += 1
    return boat