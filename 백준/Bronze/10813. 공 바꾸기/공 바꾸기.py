n, m = map(int, input().split()) # 바구니 n개, 공을 넣는 횟수 m번
basket = [i+1 for i in range(n)] # n개의 바구니

for _ in range(m):
    # i번, j번 바구니의 공 번호 바꾸기
    i, j = map(int, input().split()) 
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)