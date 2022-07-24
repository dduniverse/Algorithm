def star(i):
    if i==3:
        return ['***','* *','***']
    
    arr=star(i//3)
    stars=[]

    for a in arr:
        stars.append(a*3)
    for a in arr:
        stars.append(a+' '*(i//3)+a) # 가운데 (i/3)x(i/3)정사각형 공백
    for a in arr:
        stars.append(a*3)

    return stars

n=int(input())
print('\n'.join(star(n))) # 구분자.join(리스트)