import sys

n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))

s_num=sorted(list(set(num))) 
# 리스트 num을 집합으로 바꿔 중복을 제거한 뒤 다시 리스트로 만들어 정렬시킨다.
dic={s_num[i]:i for i in range(len(s_num))}
# s_num 길이만큼 for 반복문
# ex) s_num=[1,2,3]이면 3은 2번인덱스이고, 3보다 작은 값은 1,2두개이다.(정렬된 상태이므로)
# for 반복문의 i는 dic의 value, s_num[i]은 dic의 key
# i는 자신보다 작은 값의 개수이자 인덱스 번호, s_num[i]은 해당 값=자기자신 

for i in num:
    print(dic[i],end=' ') # 딕셔너리 dic에서 key=i인 값을 찾아 출력