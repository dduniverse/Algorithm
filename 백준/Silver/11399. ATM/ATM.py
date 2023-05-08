n = int(input()) # 사람의 수
time = list(map(int, input().split())) # 각 사람이 돈을 인출하는데 걸리는 시간

time.sort() # 오름차순 정렬

time_sum= 0 # 누적 시간
for i in range(n):
    time_sum += sum(time[:i+1]) 

print(time_sum)