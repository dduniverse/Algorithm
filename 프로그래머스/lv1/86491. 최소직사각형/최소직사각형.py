def solution(sizes):
    for s in sizes:
        s.sort()
    w = max([sizes[i][0] for i in range(len(sizes))])
    h = max([sizes[i][1] for i in range(len(sizes))])
    return w*h