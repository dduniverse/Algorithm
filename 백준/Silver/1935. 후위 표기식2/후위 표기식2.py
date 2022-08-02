n=int(input()) # 피연산자의 개수
question=input() # 후위 표기식 입력

n_list=[0]*n # n개의 피연산자에 각각 대응하는 값

for i in range(n):
    n_list[i]=int(input()) # 피연산자의 값

stack=[]

for i in question:
    if i.isalpha(): # i가 알파벳이면 i의 아스키코드-65(A의 아스키코드=알파벳의 첫번째)를 stack에 저장
        stack.append(n_list[ord(i)-65])
    else: # i가 알파벳이 아니면(=연산자이면)
        num2=stack.pop() # stack은 LIFO이므로 pop하면 늦게 들어간 순으로 리턴됨
        num1=stack.pop()

        if i=='+':
            stack.append(num1+num2)
        elif i=='-':
            stack.append(num1-num2)
        elif i=='*':
            stack.append(num1*num2)
        elif i=='/':
            stack.append(num1/num2)

print('%.2f' %stack[0]) # 소수점아래 둘째자리까지 출력