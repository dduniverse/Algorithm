# nCr = n!/(n-r)!r!

def factorial_5or2_cnt(num,t):
    cnt=0
    while num>0:
        cnt+=num//t # num을 t로 나눈 몫을 cnt에 더하기 => t의 지수=cnt
        num//=t # num을 t로 계속해서 나눠줌
    return cnt

n,m=map(int,input().split())

cnt_5=factorial_5or2_cnt(n,5)-factorial_5or2_cnt(m,5)-factorial_5or2_cnt(n-m,5) # 5의 지수
cnt_2=factorial_5or2_cnt(n,2)-factorial_5or2_cnt(m,2)-factorial_5or2_cnt(n-m,2) # 2의 지수
result=min(cnt_5,cnt_2) # 2의 지수와 5의 지수 중 작은 값이 0의 개수가 된다
print(result)