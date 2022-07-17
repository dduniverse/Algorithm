from collections import Counter
import sys

n = int(input())
num=[]

for i in range(n):
    num.append(int(sys.stdin.readline()))

mean=sum(num)/len(num)
print(round(mean)) # 평균: 소수점 첫째자리에서 반올림

num.sort()
if n>2: # 입력된 값이 2개 이상이면
    median=num[n//2]
    print(median) # 중앙값
else: print(num[0]) # 입력된 값이 1개이면 중앙값은 자신이므로 입력된 수 출력

cn=Counter(num).most_common() # 최빈값
if len(cn)>1 and cn[0][1]==cn[1][1]: # 최빈값이 2개 이상이고, 빈도횟수가 같으면
    print(cn[1][0]) # 두번째로 작은 값 출력
else:
    print(cn[0][0]) 

range=max(num)-min(num)
print(range) # 범위: 최댓값-최솟값