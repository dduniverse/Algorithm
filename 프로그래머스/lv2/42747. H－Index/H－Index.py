def solution(citations):
    citations.sort(reverse=True)
    
    for h in range(max(citations), 0, -1): # h(범위: 최대 인용 횟수부터 1까지) '역순' 순회
        count = 0  # h번 이상 인용된 논문 수
        for c_num in citations:
            if h <= c_num: # 인용 수가 h 이상이면 count +1
                count += 1
        if count >= h: # 가장 먼저 h번 이상 인용된 논문수가 h번 이상이면 리턴
            return h
    
    return 0