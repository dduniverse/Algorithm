import sys

# try~except문 사용
try: 
    while True: # 값이 입력되면 계속해서 실행
        a,b=map(int,sys.stdin.readline().split())
        print(a+b)
except: # 값이 입력되지 않으면 종료
    exit()