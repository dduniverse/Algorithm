lst=[]

for i in range(9):
    n=int(input())
    lst.append(n)

m=max(lst)
m_index=lst.index(m)+1

print(m)
print(m_index)