n, m = map(int, input().split()) # 바구니 n개, 공을 넣는 횟수 m번
basket = [0 for _ in range(n)] # n개의 바구니

# i번~j번 바구니에 k번 번호의 공 넣기
for _ in range(m):
    i, j, k = map(int, input().split()) 
    i, j = i-1, j-1
    basket[i:j+1] = [k for _ in range(j-i+1)]
    
print(*basket)