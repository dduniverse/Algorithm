i = 1
while True:
    l, p, v = map(int, input().split())
    if p==0 and l==0 and v==0:
        break
    camping = (l * (v // p)) + min((v % p), l)
    print('Case {}:'.format(i), camping)
    i += 1