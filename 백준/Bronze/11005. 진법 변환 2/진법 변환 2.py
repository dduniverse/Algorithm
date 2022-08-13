# 원하는 진법으로 바꾸려면 숫자를 나눠서 나머지를 거꾸로 읽어주면 된다.
import sys

notation='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b=map(int,sys.stdin.readline().split())
answer=''

while n!=0:
    answer+=notation[n%b]
    n=n//b

print(answer[::-1])