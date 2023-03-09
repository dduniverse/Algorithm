def solution(array, n):
    answer = 0
    array.sort()
    diff = [abs(i-n) for i in array]
    answer = array[diff.index(min(diff))]

    for i in range(len(array)):
        if (diff[i] == min(diff)) and (answer > array[diff.index(diff[i])]):
            answer = array[diff.index(diff[i])]
        
    return answer