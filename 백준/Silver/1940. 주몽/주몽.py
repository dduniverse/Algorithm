n = int(input()) # 재료의 개수
m = int(input()) # 갑옷을 만드는데 필요한 두 재료의 합
nlist = list(map(int, input().split())) # n개의 재료 고유 번호

left, right = 0, n-1 # 시작 인덱스, 끝 인덱스 
answer = 0 # 경우의 수

nlist.sort() # nlist를 정렬해준 후 투 포인터로 접근

# left와 right가 만날 때까지 반복
while left < right:
    # 두 재료의 합이 m이면
    if nlist[left] + nlist[right] == m:
        answer += 1
        left += 1
        right -= 1
    # 두 재료의 합이 m보다 작으면 left +1
    elif nlist[left] + nlist[right] < m:
        left += 1
    # 두 재료의 합이 m보다 크면 right -1
    elif nlist[left] + nlist[right] > m:
        right -= 1

print(answer)