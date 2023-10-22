n = int(input())
answer = []
for i in range(n//4):
    answer.append('long')

answer.append('int')

print(*answer)