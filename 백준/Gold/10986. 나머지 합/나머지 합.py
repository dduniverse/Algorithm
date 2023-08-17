import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 수의 개수
arr = list(map(int, input().split())) # 원본배열: n개의 수

answer = 0 # M으로 나누어 떨어지는 구간의 개수

prefix_sum = [] # 합배열 S
mdsum = [] # 합배열 S를 M으로 나눈 나머지 배열
temp = 0 # 누적합 
for i in arr:
    temp += i
    prefix_sum.append(temp) # 합배열에 누적합 저장
    
    mtemp = temp % m
    mdsum.append(mtemp) # 합배열을 m으로 나눈 나머지 저장
    
    if mtemp == 0:
        answer += 1
    
mod = [0] * m  # m으로 나눴을 때의 나머지(최소 0~2)
for i in mdsum:
    mod[i] += 1

# 같은 나머지 중 2개를 뽑는 경우 iC2
for i in mod:
    if i > 1:
        comb = (i * (i-1)) // 2
        answer += comb
        
print(answer)