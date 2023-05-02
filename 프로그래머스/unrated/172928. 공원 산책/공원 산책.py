def solution(park, routes):
    x, y = 0, 0  # 시작점
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col] == 'S':
                x, y = row, col
    print((x,y))
    op = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    
    for i in routes:
        print(i)
        dx, dy = op[i.split()[0]]
        n = int(i.split()[1])
        
        xx, yy = x, y
        canmove = True
        for _ in range(n):
            nx = xx + dx  # 이동한 위치
            ny = yy + dy  # 이동한 위치
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != 'X':
                canmove = True
                xx, yy = nx, ny
            else:
                canmove = False
                break
                
        if canmove:
            x, y = nx, ny
        
    return [x, y]
    
    
        