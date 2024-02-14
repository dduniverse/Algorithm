import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 과일 N개, 스네이크버드 초기 길이 L
hlist = list(map(int, input().split())) # 과일들의 높이

hlist.sort()

for h in hlist:
    if L >= h:
        L += 1

print(L)