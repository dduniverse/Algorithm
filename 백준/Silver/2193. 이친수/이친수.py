import sys
input = sys.stdin.readline

# D[i][0] = i자리 이친수 중 0으로 끝나는 이친수 개수
# D[i][1] = i자리 이친수 중 1로 끝나는 이친수 개수
# 0은 i-1자리 이친수의 0과 1로 끝나는 모든 경우에 붙일 수 있음
# 1은 i-1자리 이친수의 0으로 끝나는 경우에만 붙일 수 있음
# 1로 끝나는 경우에 1을 붙이면 규칙 2에 위배

n = int(input())

D = [[0 for _ in range(2)] for _ in range(n+1)]
D[1][1] = 1 # 1자리 이친수
D[1][0] = 0 # 1자리 이친수 중 0으로 끝나는 수는 없음

for i in range(2, n+1):
    D[i][0] = D[i-1][1] + D[i-1][0]
    D[i][1] = D[i-1][0]
    
print(sum(D[n]))