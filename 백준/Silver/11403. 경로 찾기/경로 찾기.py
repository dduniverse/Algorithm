import sys
input = sys.stdin.readline

n = int(input()) # 정점의 개수

# 그래프 정보
D = []
for _ in range(n):
    D.append(list(map(int, input().split())))

# i에서 k로 가는 간선이 존재하고, k에서 j로 가는 간선이 존재하면 i에서 j로 가는 간선이 존재한다.    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if D[i][k] == 1 and D[k][j] == 1:
                D[i][j] = 1

# 출력                
for d in D:
    print(*d)