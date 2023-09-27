from itertools import permutations

def solution(k, dungeons):
    answer = [] # 탐험하는 던전 수
    pdungeons = list(permutations(dungeons, len(dungeons))) # 가능한 모든 탐험 순서(순열)
    
    # 모든 경우 탐색
    for pdungeon in pdungeons:
        kcopy = k
        temp = 0 # 탐험한 던전 수
        for dungeon in pdungeon:
            # 최소 필요 피로도 보다 현재 피로도가 크거나 같으면 탐험
            if kcopy >= dungeon[0]:
                temp += 1
                kcopy -= dungeon[1]
        answer.append(temp)
        
    return max(answer) # 최대 던전 수