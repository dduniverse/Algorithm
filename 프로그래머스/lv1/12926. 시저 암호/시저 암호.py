def solution(s, n):
    answer = ''
    for i in s:
        if i.islower() and ord(i)+n > 122:
            answer += chr(96 + ((ord(i)+n)- 122))
        elif i.isupper() and ord(i)+n > 90:
            answer += chr(64 + ((ord(i)+n) - 90))
        elif i == ' ':
            answer += i
        else:
            answer += chr(ord(i)+n)
    return answer
    