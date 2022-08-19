while True:
    a,b,c=map(int,input().split())
    
    if a==0 and b==0 and c==0:
        break

    n_list=[a,b,c]
    n_list.sort() # 모든 경우가 크기순 입력이 아니므로 정렬을 해준다

    if n_list[2]**2==n_list[0]**2 + n_list[1]**2:
        print('right')
    else:
        print('wrong')