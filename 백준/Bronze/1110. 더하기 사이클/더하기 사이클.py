n=int(input())
num=n
count=0 #사이클 횟수

while True: # n=26 이면
    a=num//10 # a=26//10=2 -> 26의 앞자리 수
    b=num%10 # b=26%10=6 -> 26의 뒷자리 수
    c=(a+b)%10 # c=(2+6)%10=8 -> 26의 각 자리 수 합
    num=b*10+c # 새로운 값 68
    count=count+1 # 사이클 +1, while문 반복
    
    if num==n: # 처음 수 n이랑 같아지면
        break

print(count) # 사이클 횟수 출력