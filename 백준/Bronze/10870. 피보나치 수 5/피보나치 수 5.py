def fibo(i):
    if i==0: return 0
    if i==1: return 1
    return fibo(i-1)+fibo(i-2)

n=int(input())
print(fibo(n))