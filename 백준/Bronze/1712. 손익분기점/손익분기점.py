a,b,c=map(int,input().split()) 
# a:고정비용, b:한 대의 노트북에 들어가는 가변비용, C:노트북 가격

if b>=c:  #b가 c보다 크면 총 비용(a+i*b)은 항상 총 수입(c*i)보다 큰 값이므로 손익분기점 X
    print(-1)
else:
    print(a//(c-b)+1)

# 노트북 개수 = i
# a+i*b < c*i 일 때 손익분기점
# i > a/c-b 이므로
# i = a//(c-b) + 1 (몫 + 1 을 해줘야 '크다'는 조건 만족)
