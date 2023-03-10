def solution(s1, s2):
    intersection = set(s1).intersection(set(s2))
    return len(intersection)