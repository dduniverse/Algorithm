def solution(wallpaper):
    paper = []
    
    # '#'가 위치한 좌표를 모두 paper에 저장
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                paper.append((row, col))
    print(paper)
    
    minx = min(paper, key=lambda x:x[0])[0] # 가장 왼쪽에 위치한 x 좌표
    miny = min(paper, key=lambda x:x[1])[1] # 가장 위쪽에 위치한 y 좌표
    maxx = max(paper, key=lambda x:x[0])[0] # 가장 오른쪽에 위치한 x 좌표
    maxy = max(paper, key=lambda x:x[1])[1] # 가장 아래쪽에 위치한 y 좌표
    print(minx, miny, maxx, maxy)
    
    return [minx, miny, maxx+1, maxy+1]