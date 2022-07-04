t=int(input())

for i in range(t):
    r,s=input().split()
    r=int(r) # 반복 횟수 r이 문자형으로 들어오므로 정수형으로 바꿔줌
    new_s=''

    for c in s:
       new_s=new_s+(c*r)
    print(new_s)