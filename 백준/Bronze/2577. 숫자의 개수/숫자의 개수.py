a=int(input())
b=int(input())
c=int(input())

result=a*b*c
result=str(result)
c0=c1=c2=c3=c4=c5=c6=c7=c8=c9=0

for i in result:
    if i=='0': c0+=1
    if i=='1': c1+=1
    if i=='2': c2+=1
    if i=='3': c3+=1
    if i=='4': c4+=1
    if i=='5': c5+=1
    if i=='6': c6+=1
    if i=='7': c7+=1
    if i=='8': c8+=1
    if i=='9': c9+=1

print(c0)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)