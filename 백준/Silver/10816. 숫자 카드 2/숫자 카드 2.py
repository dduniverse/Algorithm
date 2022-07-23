import sys

n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))

n_dic={} # n_list에 있는 숫자들이 몇 번 등장했는지 저장하기 위한 딕셔너리

for i in n_list: # n_list에 있는 숫자를 하나씩 가져와 n_dic에 있는지 확인
    if i in n_dic: # 이미 n_dic에 키 값이 존재하면 한번 이상 등장했던 수 이므로 +1
        n_dic[i]+=1
    else: # 처음 등장하는 숫자이면 value를 1로 초기화
        n_dic[i]=1

for i in m_list: # m_list의 수가 n_list에 몇 개 존재하는지 확인
    if i in n_dic: # m_list의 수가 n_dic에 있으면 해당하는 value값 출력
        print(n_dic[i],end=' ')
    else: # m_list의 수가 n_dic에 없으면 0 출력
        print(0, end=' ')