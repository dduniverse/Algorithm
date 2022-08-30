# 진짜 약수: n이 a의 배수이고 a가 1과 n이 아니다.
c=int(input()) # n의 진짜 약수의 개수
yaksoo=list(map(int,input().split())) # 진짜 약수

yaksoo.sort() # 약수 크기 순 정렬

if c%2!=0:
    print(yaksoo[len(yaksoo)//2]**2) # 약수의 개수가 3개이면 2번째 약수(인덱스=1)를 제곱하면 n이 됨
else:
    print(yaksoo[0]*yaksoo[-1]) # 약수 중 제일 작은 수와 제일 큰수를 곱하면 n이 됨