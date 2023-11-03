n=int(input())

stack=[]
answer=[]
can=True # 배열을 만들 수 있는지(초기값 True로 설정)
count=1

for _ in range(n): # n개의 수를 입력받는다.
    num=int(input())

    while count<=num: # 입력된 num보다 count가 작으면 
        stack.append(count) # stack에 count를 +1씩 하면서 num까지의 숫자 추가
        answer.append('+') # answer에는 + 추가
        count+=1
    
    if stack[-1]==num: # stack에 제일 마지막에 들어온 값이 입력받은 num이랑 같으면
        stack.pop() # stack에서 pop하고
        answer.append('-') # answer에 - 추가
    else:
        can=False # 배열을 만들 수 없음

if can==False:
    print('NO')
else:
    for i in answer:
        print(i)