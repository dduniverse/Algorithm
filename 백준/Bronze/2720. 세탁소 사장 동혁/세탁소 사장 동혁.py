t = int(input())
coin = [25, 10, 5, 1] # 쿼터, 다임, 니켈, 페니
for i in range(t):
    result = [] # 돌려줄 각 동전의 개수
    c = int(input()) # 거스름돈

    for j in coin:
        result.append(c//j)
        c %= j
        
    print(*result)