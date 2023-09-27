def solution(phone_book):
    phone_book.sort() # 정렬: ['1', '2', '3', '10'] -> ['1', '10', '2', '3']
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): # 다른 번호의 접두어([:len_i])인 경우
            return False
    return True