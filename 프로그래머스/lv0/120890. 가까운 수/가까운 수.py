def solution(array, n):
    answer = 0
    array.sort()
    diff = [abs(i-n) for i in array]
    answer = array[diff.index(min(diff))]        
    return answer