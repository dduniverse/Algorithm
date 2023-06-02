def solution(n, words):
    for i in range(1, len(words)):
        last = words[i-1][-1]  # 마지막 글자
        if last != words[i][0]: # 앞사람과 다른 글자로 시작
             return [(i % n) + 1, (i // n) + 1]
            
        if len(words[i]) == 1: # 한글자일 때
            return [(i % n) + 1, (i // n) + 1]
        
        if words[i] in words[:i]: # 중복되는 단어일 때
            return [(i % n) + 1, (i // n) + 1]    
    else:
        return [0, 0]        
        