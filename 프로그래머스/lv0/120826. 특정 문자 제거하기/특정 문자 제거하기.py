def solution(my_string, letter):
    answer = ''
    lms = list(my_string)
    
    for i in lms[:]:
        if i == letter:
            lms.remove(letter)
            
    answer = ''.join(lms)
    return answer