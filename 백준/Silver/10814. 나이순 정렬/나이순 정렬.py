n=int(input())
people=[]

for i in range(n):
    age,name=input().split()
    people.append((int(age),name))

people.sort(key=lambda x:x[0]) 
# 파이썬은 기본적으로 안정정렬(stable정렬)을 한다.
# stabel 정렬: 입력받은 값들 중에서 같은 값이 있는 경우 해당 값의 순서를 그대로 유지한다.

for i in people:
    print(i[0],i[1])