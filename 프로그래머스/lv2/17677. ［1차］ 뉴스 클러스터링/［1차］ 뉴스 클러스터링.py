def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    
    A, B = [], [] # 다중집합
    for i in range(len(str1)-1):
        str = str1[i:i+2] # 두글자씩 끊어
        if str.isalpha(): # 영문자로 된 글자만 다중집합의 원소로 만듦
            A.append(str)
    for i in range(len(str2)-1):
        str = str2[i:i+2] # 두글자씩 끊어
        if str.isalpha(): # 영문자로 된 글자만 다중집합의 원소로 만듦
            B.append(str)
    if len(A) == 0 and len(B) == 0:
        j = 1
    else:
        # 다중합집합
        a_temp = A.copy()
        a_result = A.copy()
        for i in B:
            if i not in a_temp: # B에만 존재하면 합집합에 추가
                a_result.append(i) 
            else: # 공통으로 존재하면 중복되므로 제거
                a_temp.remove(i)
        # 다중교집합
        result = []
        for i in B:
            if i in A:
                A.remove(i)
                result.append(i)

        j = len(result)/len(a_result) # 자카드 유사도 = 교집합/합집합
        
    return (int(j * 65536))