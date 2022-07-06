t=int(input())

for i in range(t):
    h,w,n=map(int,input().split()) # h:호텔의 층 수, w:각 층의 방 수 n:몇번쨰 손님
    floor=n%h
    room=(n//h)+1

    if floor==0: # n이 h의 배수이면
        print((100*h)+(n//h)) # h=6, n=6 -> 601호, n=60, 610호
    elif room<10: # 10번 방 이전은 908, 1203등 08, 03 형태
        print('{}0{}'.format(floor,room))
    else: 
        print('{}{}'.format(floor,room))