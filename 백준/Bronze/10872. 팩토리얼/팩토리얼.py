def fac(i):
    if i==0: return 1
    if i==1: return 1
    return i*fac(i-1)

n=int(input())
print(fac(n))