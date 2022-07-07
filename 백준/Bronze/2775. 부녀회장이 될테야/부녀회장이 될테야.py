t=int(input())

for i in range(t):
    k=int(input()) # 층
    n=int(input()) # 호

    people=[i for i in range(1,n+1)] # 0층 각 호의 사람 수(1,2,3,...,n)

    for x in range(k): # 한 층씩 늘어날 때마다
        for y in range(1,n): # people의 값이 바뀐다.
            people[y]=people[y-1]+people[y]
    
    print(people[-1]) # k층 n호 사람 수