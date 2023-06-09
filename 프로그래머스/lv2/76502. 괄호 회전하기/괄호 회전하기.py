from collections import deque

def solution(s):
    answer = len(s)
    for i in range(len(s)): # 0부터 len(s)칸까지 회전
        queue = deque(s) # 큐로 변환
        queue.rotate(-i) # 회전     
        
        stack = [] # 스택
        for q in queue:
            if q == '(' or q == '{' or q =='[': # 열린 괄호이면 스택에 추가
                stack.append(q)
            else: # 닫힌 괄호일 때
                if stack: # 스택이 존재하면 마지막 요소와 짝 비교
                    if stack[-1] == '(' and q == ')':
                        stack.pop()
                    elif stack[-1] == '{' and q == '}':
                        stack.pop()
                    elif stack[-1] == '[' and q == ']':
                        stack.pop()   
                else: # 스택이 존재하지 않으면 추가
                    stack.append(q)
        if stack:
            answer -= 1 # 스택에 요소가 존재하면 불가능한 경우이므로 -1
            
    return answer