import sys
# 두 개의 스택을 만들어 문자열을 붙였다 뗐다 반복한다
stack1=list(sys.stdin.readline().rstrip()) # 첫번째 스택에 입력된 문자열 저장, sys.stdin.readline은 개행문자까지 입력받기 때문에 제거해준다.
stack2=[]
m=int(sys.stdin.readline()) # 명령 개수

for i in range(m):
    command=sys.stdin.readline()

    if 'P' in command:
        stack1.append(command.split()[1]) # 입력받은 문자를 stack1에 추가
    if 'L' in command:
        if stack1:
            stack2.append(stack1.pop()) # 커서를 왼쪽으로 옮기는 것이므로 stack1에서 top 문자를 pop하여 stack2에 추가한다.
        else: # stack1이 비어있으면 무시=커서가 문장의 맨 앞
            continue 
    if 'D' in command:
        if stack2:
            stack1.append(stack2.pop()) # stack2의 top에 있는 문자를 pop하여 stack1에 추가한다.
        else: # stack2가 비어있으면 무시=커서가 문장의 맨 뒤
            continue
    if 'B' in command:
        if stack1:
            stack1.pop() # 커서 왼쪽에 있는 문자 삭제=stack1의 top문자
        else: # stack1이 비어있으면 무시=커서가 문장의 맨 앞
            continue

print(''.join(stack1+list(reversed(stack2))))