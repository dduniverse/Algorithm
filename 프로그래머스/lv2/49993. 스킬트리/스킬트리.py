def solution(skill, skill_trees):
    answer = 0                      # 가능한 스킬트리 개수
    for skill_tree in skill_trees:
        temp = ''                   # 배우는 스킬 순서 저장 ex) 102, 012, 01, 12
        for st in skill_tree:
            if st in skill:
                temp += st

        # 선행 스킬 순서대로 배우면(= 스킬을 배우고 & 0번 스킬로 시작 & skill의 부분문자열이면)
        if temp and temp[0] == skill[0] and temp in skill:
            answer += 1
        # 순서에 없는 스킬들로만 구성되어 있을 때(=temp가 비어있음)
        elif temp == '':
            answer += 1
            
    return answer
        
