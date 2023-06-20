def solution(elements):
    answer = []
    elements = elements * 2
    for i in range(1, len(elements)//2+1):
        for j in range(len(elements)//2):
            answer.append(sum(elements[j:j+i]))
    return(len(set(answer)))