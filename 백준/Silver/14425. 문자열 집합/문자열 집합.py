import sys

n,m=map(int,sys.stdin.readline().split())
n_list=[]
m_list=[]

for i in range(n):
    n_list.append(sys.stdin.readline())
n_list=set(n_list)

for i in range(m):
    m_list.append(sys.stdin.readline())

c=0

for i in m_list: # m_list의 카드를 하나씩 꺼내 n_list에 있는지 확인하는 과정
    if i in n_list:
        c+=1
print(c)