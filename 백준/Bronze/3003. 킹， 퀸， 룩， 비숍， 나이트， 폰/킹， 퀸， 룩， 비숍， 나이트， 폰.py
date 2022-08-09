chess=[1,1,2,2,2,8]

have=list(map(int,input().split()))

need=[]

for c,h in zip(chess,have): # 리스트 각 요소별 빼기 연산
    need.append(c-h)

print(*need)