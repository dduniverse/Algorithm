def solution(survey, choices):
    n1, n2, n3, n4 = {'R':0, 'T':0}, {'C':0, 'F':0}, {'J':0, 'M':0}, {'A':0, 'N':0}
    
    for i in range(len(survey)):
        if survey[i] == 'RT' or survey[i] =='TR':
            if choices[i] < 4:  # 비동의 관련 선택지
                n1[survey[i][0]] += 4 - choices[i]
            elif choices[i] > 4:  # 동의 관련 선택지
                n1[survey[i][1]] += choices[i] - 4
        if survey[i] == 'CF' or survey[i] =='FC':
            if choices[i] < 4:  # 비동의 관련 선택지
                n2[survey[i][0]] += 4 - choices[i]
            elif choices[i] > 4:  # 동의 관련 선택지
                n2[survey[i][1]] += choices[i] - 4    
        if survey[i] == 'JM' or survey[i] =='MJ':
            if choices[i] < 4:  # 비동의 관련 선택지
                n3[survey[i][0]] += 4 - choices[i]
            elif choices[i] > 4:  # 동의 관련 선택지
                n3[survey[i][1]] += choices[i] - 4
        if survey[i] == 'AN' or survey[i] =='NA':
            if choices[i] < 4:  # 비동의 관련 선택지
                n4[survey[i][0]] += 4 - choices[i]
            elif choices[i] > 4:  # 동의 관련 선택지
                n4[survey[i][1]] += choices[i] - 4
    
    answer = ''
    answer += 'R' if n1['R'] >= n1['T'] else 'T'
    answer += 'C' if n2['C'] >= n2['F'] else 'F'
    answer += 'J' if n3['J'] >= n3['M'] else 'M'
    answer += 'A' if n4['A'] >= n4['N'] else 'N'
    return answer