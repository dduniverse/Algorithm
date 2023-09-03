import sys
input = sys.stdin.readline

n = int(input())

T = [0 for _ in range(n+1)]  # 기간
P = [0 for _ in range(n+1)]  # 금액
D = [0 for _ in range(n+2)]  # i일부터 퇴사일까지의 최대 수익(n+1: 퇴사일)

for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())

# n일부터 거꾸로 계산해옴(n일~퇴사일 수익 < 1일~퇴사일 수익)
for i in range(n, 0 , -1):
    if T[i] + i > n+1:
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1], D[i+T[i]]+P[i])

print(D[1])