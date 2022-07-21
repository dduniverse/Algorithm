import sys

a,b=map(int,sys.stdin.readline().split())

a_set=set(map(int,sys.stdin.readline().split()))
b_set=set(map(int,sys.stdin.readline().split()))

print(len(a_set ^ b_set)) # 대칭차집합