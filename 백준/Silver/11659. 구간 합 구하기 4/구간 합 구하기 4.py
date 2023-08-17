import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 데이터의 개수, 질의 개수
a = list(map(int, input().split())) # 구간 합을 구할 배열

# 합 배열 구하기
s = [0] * (N+1) # 합 배열
for n in range(1, N+1):       
    s[n] = s[n-1] + a[n-1]

# i에서 j까지의 구간 합        
for _ in range(M):
    i, j = map(int, input().split())
    print(s[j] - s[i-1])