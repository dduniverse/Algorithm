def solution(s):
    flag = False
    stack = []
    for i in s:
        if i == ')': # 닫힌 괄호일 때
            if stack and stack[-1] == '(': # stack이 존재하고, 마지막 요소가 열린 괄호일때
                stack.pop()
                flag = True
            else: # 아니면 stack에 추가
                stack.append(i)
        else: # 열린 괄호이면 stack에 추가
            stack.append(i)
            
    if stack: # 모든 과정이 끝났는데 stack에 남아있는 것이 있으면 올바르지 않은 괄호임
        flag = False
            
    return flag