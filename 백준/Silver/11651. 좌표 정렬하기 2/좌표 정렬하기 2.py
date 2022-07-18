n=int(input())
point=[]

for _ in range(n):
    x,y=map(int,input().split())
    point.append((x,y))

point.sort(key=lambda x:(x[1],x[0])) # 정렬기준: key=lambda 함수 사용, point의 1열을 기준으로 정렬하기

for i in point:
    print(i[0],i[1])