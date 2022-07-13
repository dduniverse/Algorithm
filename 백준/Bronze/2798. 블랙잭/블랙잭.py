n,m=map(int,input().split())
card=list(map(int,input().split())) # 카드에 쓰여있는 수

sum=0
sum_list=[]

for a in range(n): # 카드 n개에서 3개를 뽑는 과정
    for b in range(a+1,n): # 위에서 뽑은 한 개를 뺀 나머지 중 1개
        for c in range(b+1,n): # 위에서 뽑은 두 개를 뺀 나머지 중 1개
            sum=card[a]+card[b]+card[c]
            if sum<=m:
                sum_list.append(sum)

print(max(sum_list))