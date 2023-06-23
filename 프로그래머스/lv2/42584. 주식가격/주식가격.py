def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    stack = [] # 상승중인 가격을 저장하는 스택
    for i, price in enumerate(prices):
        # stack에 있는 가격들이 지금 들어온 price보다 작으면 계속해서 실행(while)
        while stack and stack[-1][1] > price: # 스택 존재 &, 마지막 가격이 현재가보다 높으면
            idx, p = stack.pop() # 스택에서 pop
            answer[idx] += i - idx # 몇초간 가격이 떨어지지 않는지 계산
            
        stack.append((i, price)) # 가격 계산이 끝나면 스택에 현재가 추가
    
    for i, price in stack: # 스택에 남아있는 가격들에 대해 유지되는 시간 계산
        answer[i] = len(prices)-(i+1)
        
    return answer