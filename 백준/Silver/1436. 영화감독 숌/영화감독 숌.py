n = int(input())
title=666
c=0

while(True):
    if "666" in str(title) : # title에 666이라는 수가 있으면
        c+=1 # 횟수 +1
        if c==n: # n번째이면
            print(title) # title 출력
            break
    
    title+=1 # title을 1씩 증가시키며 while문 반복 확인