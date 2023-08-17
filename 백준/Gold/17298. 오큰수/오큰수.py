n = int(input()) # 수열 A의 크기
arr = list(map(int, input().split())) # 수열 A의 N개의 수

stack = []
answer = [-1] * n # 오큰수
for i in range(n):
    while stack and stack[-1][1] < arr[i]: # 오큰수 조건
        idx, value = stack.pop()
        answer[idx] = arr[i] # answer의 해당 idx 위치에 오큰수 저장장
    stack.append((i, arr[i])) # (idx, value) 추가

print(*answer)