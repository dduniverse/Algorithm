n=int(input())

# 시간초과를 피하기 위해 for문 사용
a,b=0,1
for i in range(n):
    a,b=b,a+b

print(a)