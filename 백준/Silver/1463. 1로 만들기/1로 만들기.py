import sys
input = sys.stdin.readline

n = int(input())

# DP 테이블 = i를 1로 만드는 최소 연산 횟수
D = [0] * (n+1)
D[1] = 0

for i in range(2, n+1):
    # i-1에 1을 더한 값
    D[i] = D[i-1] + 1
    # 2의 배수이면 i//2에 1을 더한 값과 i-1에 1을 더한 값 중 작은 값으로 업데이트
    if i % 2 == 0:
        D[i] = min(D[i], D[i//2]+1)
    # 3의 배수이면 i//3에 1을 더한 값과 i-1에 1을 더한 값 중 작은 값으로 업데이트
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3]+1)
        
print(D[n])