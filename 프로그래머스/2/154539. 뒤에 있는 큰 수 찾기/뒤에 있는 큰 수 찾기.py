def solution(numbers):  
    stack = [] # (idx, value) 형태로 저장
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        # 스택에 있는 수보다 내가 더 크면
        while stack and stack[-1][1] < numbers[i]:
            idx, value = stack.pop() # 스택에서 꺼내고
            answer[idx] = numbers[i] # answer의 꺼낸 수의 idx 위치에 numbers[i] 저장
            
        stack.append((i, numbers[i])) # (idx, value) 추가

    return answer