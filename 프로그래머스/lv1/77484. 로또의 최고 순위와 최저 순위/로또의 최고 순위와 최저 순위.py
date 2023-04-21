def solution(lottos, win_nums):
    answer = [0,0] # 최고순위, 최저순위
    c = 0 # 일치한 숫자 개수
    n = lottos.count(0) # 알아볼 수 없는 번호(0) 개수
    lot = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    for i in lottos:
        if i in win_nums:
            c += 1
    
    answer[0], answer[1] = lot[c+n], lot[c]
    return answer