n, k = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

coin = 0 # 동전의 개수
for i in range(1, n+1): # array의 뒤에서부터(=큰 값부터)
    if (k != 0) and ((k // array[-i]) > 0): # k가 0이 아니고, array[i]로 나눈 몫이 존재하면
        coin += (k // array[-i]) # 몫을 coin에 누적
        k %= array[-i] # k를 나머지로 바꿈

print(coin)