import sys
import heapq
input = sys.stdin.readline

n = int(input()) # n장의 카드
heap = []
for _ in range(n):
    x = int(input())
    if x != 0: # x가 0이 아니면 추가
        heapq.heappush(heap, (abs(x), x)) # (절댓값, 실제값)으로 추가
    else: # x가 0이면 절댓값이 가장 작은 값을 출력
        if heap:
            print(heapq.heappop(heap)[1])
        else: # 배열이 비여있으면 0을 출력
            print(0)