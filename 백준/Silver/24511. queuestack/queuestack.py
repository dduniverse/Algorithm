from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) # queuestack을 구성하는 N개의 자료구조
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque([])
for i in range(N):
    if A[i] == 0: # 큐인 자료구조만 queue에 추가
        queue.append(B[i])

for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end= ' ')