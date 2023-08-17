n = int(input())
score = list(map(int, input().split()))

m = max(score) # 최댓값
avg = sum(score) * 100 / m / n # 변환 점수의 평균을 구하는 식(A+B+C)*100/m/n
print(avg)