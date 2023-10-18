def solution(k, d):
    answer = 0
    
    # x**2 + y**2 = d**2 -> y = (d**2 - x**2) ** 0.5
    for x in range(0, d+1, k):
        y = int((d**2 - x**2) ** 0.5) # x 좌표마다 가능한 y 좌표를 찾음
        answer += len(range(0, y+1, k)) # 0부터 y까지 k스텝으로 가능한 점의 개수
        
    return answer