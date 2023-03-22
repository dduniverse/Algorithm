def solution(s):
    if len(s) == 4 or len(s) == 6:
        return all([i.isdigit() for i in s])
    return False