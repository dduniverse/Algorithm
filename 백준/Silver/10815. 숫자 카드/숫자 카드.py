import sys

n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))

n_list.sort()

for i in m_list: # m_list의 카드를 하나씩 꺼내 n_list에 있는지 확인하는 과정
    start, end = 0, n-1

    while start<=end: # end보다 start가 작으면 계속해서 반복
        mid=(start+end)//2 # mid는 start와 end의 중간값
        if n_list[mid]==i: # n_list의 mid인덱스 값이 i와 같으면 1 출력
            print(1,end=' ')
            break
        elif n_list[mid]<i: # n_list의 mid인덱스 값이 i보다 작으면 start를 mid+1값으로 바꾼다
            start=mid+1
        else: # n_list의 mid인덱스 값이 i보다 크면 end를 mid-1로 바꾼다
            end=mid-1
        if start>end: # start가 end보다 커지면 0 출력
            print(0,end=' ')
            break