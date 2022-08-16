x,y,w,h=map(int,input().split()) # (x,y):현 위치 (w,h): 직사각형 오른쪽 위 꼭짓점


distance=min(h-y, w-x, x-0, y-0)

if distance < 0:
    print(-distance)
else:
    print(distance)