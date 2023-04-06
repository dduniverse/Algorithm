def solution(answers):
    supoza1 = [1,2,3,4,5]
    supoza2 = [2,1,2,3,2,4,2,5]
    supoza3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    for i, v in enumerate(answers):
        if v == supoza1[i % len(supoza1)]:
            score[0] += 1
        if v == supoza2[i % len(supoza2)]:
            score[1] += 1
        if v == supoza3[i % len(supoza3)]:
            score[2] += 1
    
    return sorted([i+1 for i in range(len(score)) if max(score) == score[i]])