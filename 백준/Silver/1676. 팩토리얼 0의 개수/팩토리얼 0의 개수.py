def facotrial(i):
    if i==0 or i==1:
        return 1
    for _ in range(i):
        return i*facotrial(i-1)

n=int(input())
fac=facotrial(n)
fac=list(str(fac))
fac.reverse()
c=0
for i in fac:
    if i=='0':
        c+=1
    if i!='0':
        break
print(c)