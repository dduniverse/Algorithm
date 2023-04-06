def solution(name, yearning, photo):
    nydict = dict(zip(name, yearning))
    for pho in photo:
        for p in range(len(pho)):
            if pho[p] in nydict:
                pho[p] = nydict[pho[p]]
            else:
                pho[p] = 0
        pho = sum(pho)
    return [sum(pho) for pho in photo]