n,m=map(int,input().split())
n_list=[]
m_list=[]

for _ in range(n):
    n_list.append(input())
for _ in range(m):
    m_list.append(input())

nm_list=list(set(n_list) & set(m_list)) # 중복을 제거한 n과 m의 교집합 리스트

print(len(nm_list))
for i in sorted(nm_list):
    print(i)