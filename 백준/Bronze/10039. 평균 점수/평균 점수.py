score=[]
for i in range(5):
    s=int(input())

    if s>40:
        score.append(s)
    else:
        score.append(40)

print(int(sum(score)/5))