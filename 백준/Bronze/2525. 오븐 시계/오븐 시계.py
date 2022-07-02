A,B=map(int, input().split())
C=int(input())

if B+C<60:
    print(A,B+C)
elif B+C>=60: # 분의 합(B+C)이 60분이 넘으면
    A=A+(B+C)//60 # B+C를 60으로 나눈 몫을 A에 더하기
    min=(B+C)%60 # B+C를 60으로 나눈 나머지를 새로운 분(min)으로 설정
    if A>=24: # 이때 A의 값이 24(0시) 이상이면
        A=A-24 # A-24를 A로 ex. 25시 -> 1시
    print(A,min)