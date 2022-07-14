n=int(input())
list=[]

for i in range(n):
    x,y=map(int,input().split())
    list.append((x,y))

for a in list:
    rank=1
    for b in list:
        if a[0]<b[0] and a[1]<b[1]: # 본인보다 덩치가 큰 사람의 수 만큼 +1
            rank=rank+1
    print(rank,end=' ')