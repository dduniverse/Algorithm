a=[]

for i in range(10):
    n=int(input())
    a.append(n%42)

a=set(a) # set은 값의 중복을 허용하지 않음
print(len(a))