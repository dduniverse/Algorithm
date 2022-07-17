import sys

n = int(sys.stdin.readline())
num=[0]*10001 # 10001개의 0으로 채워진 리스트

for i in range(n): # n개의 수 입력받기
    num[int(sys.stdin.readline())]+=1 # 입력받은 숫자가 몇번 들어왔는지 num 리스트의 각 인덱스에 체크

for i in range(10001):
    if num[i]!=0: # 0이 아니면
        for j in range(num[i]): # 해당 인덱스의 값 만큼(= 해당 숫자가 입력된 횟수) 그 수를 출력한다.
            print(i)
