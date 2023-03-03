def solution(my_string, letter):
    answer = ''
    answer = ''.join([i for i in my_string if i not in letter])
    return answer