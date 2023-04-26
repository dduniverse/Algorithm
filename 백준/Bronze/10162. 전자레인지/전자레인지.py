button = [300, 60, 10] # 5분, 1분, 10초

t = int(input()) # 요리 시간

result = []
if t % 10 != 0: # 가장 작은 단위인 10초로 단위가 아니면 불가능한 시간임
    print(-1)
else:
    for i in button:
        result.append(t // i)
        t %= i
    print(*result)