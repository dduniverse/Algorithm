import math

a,b,v=map(int,input().split())
# v=day(a-b)+a -> (day)일 동안 a-b만큼 올라가고, 마지막 날 a만큼 올라가고서 더이상 떨어지지 않는다.
# day=(v-a)(a-b) 
day=(v-a)/(a-b)+1 # 마지막날 a만큼 올라가는 것을 고려하여 하루를 추가해준다. +1
day=math.ceil(day) # math의 ceil()함수:올림

print(day)