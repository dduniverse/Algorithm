def solution(k, score):
    answer = [] # 발표 점수
    legend = [] # 명예의 전당
    for i in range(len(score)):
        legend.append(score[i])
        legend.sort(reverse=True)
        legend = legend[:k]
        answer.append(legend[-1])
    return answer