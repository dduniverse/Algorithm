n = int(input()) # 수의 개수
nlist = list(map(int, input().split())) # n개의 수

answer = 0 # 경우의 수

nlist.sort()

for i in range(n):
    temp = nlist[:i] + nlist[i+1:] # i를 제외한 리스트
    start, end = 0, len(temp)-1

    while start < end:
        # 두 수의 합이 nlist[i]이면 경우의 수 +1
        if temp[start] + temp[end] == nlist[i]:
            answer += 1
            break
        # 두 수의 합이 nlist[i]보다 작으면 start +1
        elif temp[start] + temp[end] < nlist[i]:
            start += 1
        # 두 수의 합이 nlsit[i]보다 크면 end -1
        else:
            end -= 1

print(answer)