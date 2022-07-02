import sys

n=int(sys.stdin.readline())

for i in range(n):
    t1,t2=map(int, sys.stdin.readline().split())
    print('Case #{}: {} + {} = {}'.format(i+1,t1,t2,t1+t2))