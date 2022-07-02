import sys # sys.stdin.readline()을 사용하기 위한 모듈 import

n=int(input())

for i in range(n):
    t1,t2=map(int, sys.stdin.readline().split()) # input 대신 sys.stdin.readline() 사용
    print(t1+t2)