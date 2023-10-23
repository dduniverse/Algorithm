n, m = map(int, input().split())
basket = [i+1 for i in range(n)]

# i~j번 바구니 역순으로
for _ in range(m):
    i, j = map(int, input().split()) 
    temp = basket[i-1:j]
    basket[i-1:j] = temp[::-1]

print(*basket)