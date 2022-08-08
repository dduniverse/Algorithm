def facotrial(i):
    if i==0 or i==1:
        return 1
    for _ in range(i):
        return i*facotrial(i-1)

n=int(input())
print(facotrial(n))