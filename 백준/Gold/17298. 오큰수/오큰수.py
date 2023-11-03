n = int(input())
A = list(map(int, input().split()))

nge = [-1 for _ in range(n)] # 오큰수
stack = []
for i, a in enumerate(A):
    # 스택의 마지막 원소보다 a가 크면 pop 연산 및 오큰수 저장
    while stack and stack[-1][1] < a:
        idx, value = stack.pop()
        nge[idx] = a
    
    stack.append((i, a)) # (인덱스, 원소) 형식으로 추가

print(*nge)