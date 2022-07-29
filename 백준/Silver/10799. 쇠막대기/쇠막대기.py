bar=input()

stack=[]
count=0 # 잘린 막대기의 개수

# () 여는괄호 닫는괄호가 연속으로 나오면 레이저
for i in range(len(bar)):
    if bar[i]=='(': # 현재 왼쪽 괄호이면 stack에 추가
        stack.append(bar[i])
    else: # 현재 오른쪽 괄호이면 앞의 상황을 파악
        if bar[i-1]=='(': # 바로 앞이 여는 괄호 였으면 이는 레이저이다.
            stack.pop() # 막대기의 시작점으로 생각했던 여는 괄호 하나를 stack에서 빼주고
            count+=len(stack) # stack에 있는 막대기 개수만큼 count에 추가해준다
        elif bar[i-1]==')': # 바로 앞이 닫는 괄호 였으면 현재는 막대기의 끝부분이다.
            stack.pop() # 막대기 하나가 모두 끝났으므로 여는 괄호 하나를 stack에서 제거해주고
            count+=1 # count +1을 해준다.
print(count)