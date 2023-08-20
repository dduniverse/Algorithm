a, b = map(int, input().split())
    
# 최대 공약수 구하기(유클리드 호제법)
while a % b > 0:
    a, b = b, a % b   
gcd = b

print('1' * gcd)