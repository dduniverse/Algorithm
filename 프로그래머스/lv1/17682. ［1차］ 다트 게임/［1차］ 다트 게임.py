import re

def solution(dartResult):  
    dr = re.split('([0-9][0-9]?[A-Z][#|*]?)', dartResult)
    dr = ' '.join(dr).split()
    # print(dr)
    
    num = []
    for i in dr:
        n = 0
        for j in range(len(i)):
            if i[j] == 'S':
                n = (int(i[:j]) ** 1)
            if i[j] == 'D':
                n = (int(i[:j]) ** 2)
            if i[j] == 'T':
                n =(int(i[:j]) ** 3)
        num.append(n)
    # print(num)
    
    for i in range(len(dr)):
        if '*' in dr[i]:
            if i == 0:
                num[i] *= 2
            else:
                num[i] *= 2
                num[i-1] *= 2
        if '#' in dr[i]:
            num[i] *= (-1)
    # print(num)
    return sum(num)    
            