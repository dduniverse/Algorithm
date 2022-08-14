a,b=map(int,input().split()) # a진법, b진법
m=int(input()) # a진법을 이루고 있는 숫자 m개
m_list=list(map(int,input().split()))

sum=0 # a진법 -> 10진법으로 바꾼 수
for i in range(m):
    sum+=m_list[i]*(a**(m-i-1))

result=[]
while sum:
    result.append(str(sum%b)) # join을 위해 나머지를 문자열로 저장
    sum=sum//b

result=result[::-1]
result=' '.join(result) # 출력시 띄어쓰기를 해주기 위해 공백을 기준으로 join

print(result)