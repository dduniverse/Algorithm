H,M=map(int,input().split())

if M>=45:
    print(H, M-45)
elif H>0 and M<45: # M이 45분 보다 적으면 -45분은 +15분과 같음 
    print(H-1, M+15)
else: # 시간이 0시이면 23시로
    print(23, M+15)