def solution(id_pw, db):
    for id, pw in db:
        if id_pw[0] == id: 
            if id_pw[1] == pw: # id, pw 모두 일치
                return 'login'
            else: # id 일치, pw 불일치
                return 'wrong pw'
    return 'fail' # 아무 조건에도 해당되지 않을 때