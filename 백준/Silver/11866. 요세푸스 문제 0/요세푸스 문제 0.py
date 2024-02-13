from collections import deque
n, k = map(int, input().split()) # N명의 사람, K번째 사람 제거

nlist = deque([i for i in range(1, n+1)])

del_num = [] # 원에서 제거된 순서

# N명의 모든 사람이 제거될 때까지 반복
while nlist:
    nlist.rotate(-(k-1)) # -(k-1)번 회전 후
    del_num.append(str(nlist.popleft())) # 맨 앞에 위치한 수 popleft

# 요세푸스 순열 출력
print('<' + ', '.join(del_num) + '>')