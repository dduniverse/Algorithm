# 10진수로 바꿀 때
# ex) 2진수 1011 -> 각 자리에 2^3, 2^2, 2^1, 2^0을 곱해주고 그 값들을 모두 더함
import sys

notation='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n,b=sys.stdin.readline().split()

result=0
for i in range(len(n)):
    spot=notation.index(n[i])*(int(b)**(len(n)-i-1))
    result+=spot

print(result)