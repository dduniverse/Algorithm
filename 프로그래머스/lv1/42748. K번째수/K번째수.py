def solution(array, commands):
    answer = []
    for com in commands:
        slice = array[com[0]-1:com[1]]
        slice.sort()
        answer.append(slice[com[2]-1])
    return answer