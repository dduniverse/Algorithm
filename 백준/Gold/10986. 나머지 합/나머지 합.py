n, m = map(int, input().split()) # n개의 수, M으로 나누기
A = list(map(int, input().split())) # n개의 수로 이루어진 원본 배열

S = [] # 합 배열
M = [] # 합 배열 S를 M으로 나눈 나머지

answer = 0 # M으로 나눠지는 (i, j) 쌍의 개수

temp = 0
for i in A:
    temp += i
    S.append(temp) # 누적 합
    
    M.append(temp % m) # 누적 합 % m
    
    # 나누어 떨어지면(i에서 i 구간) answer +1
    if temp % m == 0:
        answer += 1
    
# (i, j) 구간 합이 m으로 나누어 떨어지면
# (S[j]-S[i-1]) % m == 0 이므로 S[j] % m == S[i-1] % m 
# 즉, M[j] == M[i-1]이면 (i, j) 구간 합이 m으로 나누어 떨어진다
# 누적합의 나머지가 같은 인덱스 중에 2개를 뽑는 경우의 수 

# 나머지의 개수 파악(m=3이면 나머지는 0, 1, 2 셋 중 하나)
mod_count = [0] * m
for i in M:
    mod_count[i] += 1
    
for i in mod_count:
    answer += i * (i-1) // 2 # i개 중에 2개를 뽑는 경우의 수(2C1)

print(answer)