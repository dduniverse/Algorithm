n,m=map(int,input().split())
chess=[]
count=[]

for _ in range(n):
    chess.append(input())

for i in range(n-7): # 8x8 형태로 자를 시작점 찾기
    for j in range(m-7):
        wh=0 # 흰색으로 시작했을 때 새로 색칠한 수
        bl=0 # 검은색으로 시작했을 때 새로 색칠한 수
        for a in range(i,i+8): # 8x8 형태로 자르기
            for b in range(j,j+8):
                if (a+b)%2==0: # 행열의 인덱스 합이 짝수이면 = 시작점과 같은색으로 칠해야함.
                    if chess[a][b]!='W': # 해당 위치가 흰색이 아니면=검은색이면
                        wh=wh+1 # 흰색으로 시작했을 때 짝수번째는 같은 흰색이어야 하므로 칠하는 횟수 +1
                    else: # 해당 위치가 흰색이면
                        bl=bl+1 # 검은색으로 시작했을 때 짝수번째는 같은 검은색이어야 하므로 칠하는 횟수 +1
                else: # 행열의 인덱스 합이 홀수이면 = 시작점과 다른색으로 칠해야함.
                    if chess[a][b]!='B': # 해당 위치가 검은색이 아니면=흰색이면
                        wh=wh+1 # 흰색으로 시작했을 때 홀수번째는 검은색이어야 하므로 칠하는 횟수 +1
                    else: # 해당 위치가 검은색이면
                        bl=bl+1  # 검은색으로 시작했을 때 홀수번째는 흰색이어야 하므로 칠하는 횟수 +1
        count.append(min(wh,bl)) # 시작점에 따라 어느색으로 시작했을 때 더 적게 칠하는지 구해 count에 저장

print(min(count)) # 모든 경우의 수를 다 체크한 후 count중 가장 작은 수 출력