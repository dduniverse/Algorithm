import sys
input = sys.stdin.readline

n = int(input()) # 수의 개수
    
# 10001 크기의 num 값을 인덱스(id)로 하는 리스트 idx
idx = [0] * 10001 # n개의 수는 10,000 이하의 수임
for i in range(n):
    idx[int(input())] += 1

# idx를 처음부터 끝까지 탐색하면서 해당 값이 존재하면 id(=num값) 출력
for id in range(10001):
    if idx[id] > 0:
        for _ in range(idx[id]):
            print(id)
            