from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    fail = list(p-c)
    return fail[0]