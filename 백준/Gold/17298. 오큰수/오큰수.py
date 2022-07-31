import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

stack=[] # 인덱스 번호
res=[-1]*n # 미리 n개의 -1로 된 배열을 생성함

for i in range(n):
    while len(stack)>0 and a[stack[-1]]<a[i]:
        res[stack.pop()]=a[i]
    
    stack.append(i)

print(*res) # *을 리스트 앞에 붙여 출력하면 원소들을 자동으로 띄어쓰기해서 출력해줌