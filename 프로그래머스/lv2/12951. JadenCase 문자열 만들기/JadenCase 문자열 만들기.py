def solution(s):
    s_list = s.split(' ') # 공백(' ') 기준 분리 -> 공백문자가 연속으로 나올 수 있기 때문에 기준split 기준을 명확히 해주어야 함
    for i in range(len(s_list)):
        s_list[i] = s_list[i].capitalize()
    return ' '.join(s_list)
        