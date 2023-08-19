n, k = map(int, input().split()) # 동전 n개, K원
coins = [int(input()) for _ in range(n)] # 동전의 가치(오름차순 입력)
coins.sort(reverse=True) # 내림차순 정렬

c = 0  # 필요한 동전 개수의 최솟값
for coin in coins:
    c += k // coin  # 몫
    k %= coin  # 나머지

print(c)