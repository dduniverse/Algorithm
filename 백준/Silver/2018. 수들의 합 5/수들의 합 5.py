n = int(input())

left, right = 0, 0 # 투 포인터
sum = 0 # left ~ right 까지의 합
answer = 0 # 가짓수

# right가 n이 될 때까지 반복
while right <= n:
    # 합이 n이면
    if sum == n:
        answer += 1 # 가짓수 +1
        right += 1
        sum += right
    # 합이 n보다 작으면 right 포인터 오른쪽으로 한 칸 이동
    elif sum < n:
        right += 1
        sum += right
    # 합이 n보다 크면 left 포인터 오른쪽으로 한 칸 이동
    elif sum > n:
        sum -= left
        left += 1

print(answer)