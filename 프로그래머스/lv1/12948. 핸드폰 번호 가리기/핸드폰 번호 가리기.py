def solution(phone_number):
    pn = list(phone_number)
    pn[:-4] = '*' * len(pn[:-4])
    return ''.join(pn)