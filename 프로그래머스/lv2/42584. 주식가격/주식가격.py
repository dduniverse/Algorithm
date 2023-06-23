def solution(prices):
    n = len(prices)
    answer = [0 for _ in range(n)]
    stack = []
    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            idx, p = stack.pop()
            answer[idx] += i - idx
            
        stack.append((i, price))
    
    for i, price in stack:
        answer[i] = n-(i+1)
        
    return answer