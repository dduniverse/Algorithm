coin = [500, 100, 50, 10, 5, 1]

t = 1000 - int(input()) # 잔돈

result = 0
for c in coin:
    if t != 0 and t//c > 0:
        result += t // c
        t %= c
print(result)