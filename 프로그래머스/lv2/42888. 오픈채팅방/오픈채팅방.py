def solution(record):
    answer = [] # 채팅방 기록
    id_name = {} # 유저 아이디: 닉네임
    
    for i in record:
        if 'Enter' in i:
            id_name[i.split()[1]] = i.split()[2]
            answer.append('+' + i.split()[1])
        elif 'Change' in i:
            id_name[i.split()[1]] = i.split()[2]
        else:
            answer.append('-' + i.split()[1])
                
    for i in range(len(answer)):
        if '+' in answer[i]:
            answer[i] = id_name[answer[i][1:]]+'님이 들어왔습니다.'
        else:
            answer[i] = id_name[answer[i][1:]]+'님이 나갔습니다.'
    
    return answer