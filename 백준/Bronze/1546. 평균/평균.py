n=int(input())
score=list(map(int, input().split()))
new_score=[]

for i in score:
    s=i/max(score)*100
    new_score.append(s)

print(sum(new_score)/len(new_score))