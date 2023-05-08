n = int(input()) # 회의 개수
meetings = [] # 회의 정보

for _ in range(n):
    start, end = map(int, input().split(" "))
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0])) # 종료시간 기준 정렬 후 같으면 시작시간 기준 오름차순 정렬

time = 0 # 끝나는 시간
answer = 0 # 회의 개수
for meeting in meetings:
    if time <= meeting[0]: # 시작시간이 끝나는 시간보다 크거나 같으면(=늦게 시작하면)
        time = meeting[1] # 끝나는 시간 갱신
        answer += 1 # 개수+1

print(answer)