c=int(input())

for i in range(c):
    std=list(map(int,input().split()))
    sum=0
    c=0
    upper=[]

    for j in range(std[0]):
        sum=sum+std[j+1]
    
    std_mean=sum/std[0]

    for j in range(std[0]):
        if std[j+1]>std_mean:
            c=c+1
    
    print('{:.3f}%'.format(c/std[0]*100))