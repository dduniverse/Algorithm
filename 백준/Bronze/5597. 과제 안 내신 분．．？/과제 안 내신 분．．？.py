num = [0 for _ in range(30)] # 출석번호

# 제출한 학생
for _ in range(28):
    n = int(input())
    num[n-1] = 1

# 제출하지 않은 학생
for i, n in enumerate(num):
    if n == 0:
        print(i+1)