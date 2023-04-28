n = int(input()) # 좌석 수
seat = input() # 좌석 정보

couple = seat.count('LL')

if couple <= 1:
    print(n)
else:
    print(n - couple + 1)