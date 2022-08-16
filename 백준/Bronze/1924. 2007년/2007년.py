day=0
month=[31,28,31,30,31,30,31,31,30,31,30,31]
week=['SUN','MON','TUE','WED','THU','FRI','SAT']

x,y=map(int,input().split())

for i in range(x-1):
    day+=month[i] # 직전 달까지의 일수를 모두 day에 더해주고(1월은 1일의 요일이 주어져 있으므로 굳이 for문으로 구할 필요가 없다)

day=(day+y)%7 # 구하려는 y일을 추가로 더해 7로 나눈 나머지가 요일의 인덱스가 된다

print(week[day])