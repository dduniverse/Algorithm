import heapq

def solution(scoville, K):
    answer = 0 # 섞은 횟수
    heapq.heapify(scoville) # 최소 heap
    
    # 새로운 스코빌 지수 계산이 가능할 때(len >= 2)
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        # 최소값이 K 이상이면 반복문 종료
        if min1 >= K:
            return answer
        # 최소값이 K 미만이면 새로운 스코빌 지수 계산
        else: 
            min2 = heapq.heappop(scoville)
            new = min1 + (min2 * 2) 
            heapq.heappush(scoville, new)
            answer += 1
    
    # 마지막으로 하나의 음식만 남았을 때
    if scoville[0] >= K:
        return answer
    else:
        return -1