import sys

n,m=map(int,sys.stdin.readline().split())

poke_name={} # key:이름, value:번호
poke_num={} # key:번호, value:이름

num=1
for _ in range(n):
    name=sys.stdin.readline().rstrip() # sys.stdin.readline은 입력받을 때 개행문자(\n)도 함께 받아오기 때문에 rstrip()을 통해 문자열 오른쪽의 개행문자를 제거해주어야 한다.
    poke_name[name]=num
    poke_num[num]=name
    num=num+1 # num을 1씩 증가시키면서 딕셔너리에 들어온 순서대로 저장

for _ in range(m):
    question=sys.stdin.readline().rstrip()
    if question.isdigit(): # 입력받은 문제가 숫자이면 poke_num에서 해당하는 숫자 key에 대한 value(이름) 출력
        print(poke_num[int(question)])
    else: # 입력받은 문제가 숫자가 아니면(=문자열이면) poke_name에서 해당하는 이름 key에 대한 value(번호) 출력
        print(poke_name[question])