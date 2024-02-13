n = int(input()) # 학생들의 수
student = list(map(int, input().split())) # 대기하는 학생들의 번호표

stack = [] # 스택
target = 1 # 타겟 넘버(1부터 N까지 순차적으로 증가)

while student: # 대기하는 학생 번호가
    if target == student[0]: # 타겟 넘버와 같으면
        student.pop(0)
        target += 1
    else: # 타켓 넘버와 다르면 스택에 추가
        stack.append(student.pop(0))

    while stack: # 스택에 수가 있을 경우
        if stack[-1] == target: # top에 있는 값이 타켓 넘버와 같으면
            stack.pop()
            target += 1
        else: # 그렇지 않으면 불가능한 경우임
            break

print('Sad' if stack else 'Nice')