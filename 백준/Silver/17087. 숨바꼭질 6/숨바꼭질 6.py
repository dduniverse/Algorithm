import math   

def gcd_n(arr): # 여러 수의 최대공약수 구하기
    gcd=arr[0] # 0번 인덱스 값을 gcd에 먼저 저장
    for item in arr:
        gcd=math.gcd(gcd,item) # gcd와 arr에서 가져온 요소의 gcd 구하기
    return gcd

n,s=map(int,input().split()) # 동생 n명, 수빈이의 현재 위치 s
a_list=list(map(int,input().split()))# 동생 n명의 위치

for i in range(len(a_list)):
    a_list[i]=a_list[i]-s
    if a_list[i]<0:
        a_list[i]=(-a_list[i]) # 동생위치-수빈현위치가 0보다 작으면 -를 붙여 양수로 바꿔주기
    else:
        pass

print(gcd_n(a_list)) # 동생위치-수빈현위치의 최대공약수 구하기