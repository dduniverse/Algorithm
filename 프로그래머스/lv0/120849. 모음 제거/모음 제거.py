def solution(my_string):
    answer = ''
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in aeiou:
            answer += i
    return answer