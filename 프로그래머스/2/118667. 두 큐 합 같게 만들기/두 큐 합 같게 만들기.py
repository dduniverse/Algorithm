from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2) # 각 큐의 합
    count = len(queue1) + len(queue2) + 2 # 최대 이동 횟수
    answer = 0
    

    
    while sum1 != sum2:
        # 한 쪽 큐가 비는 경우(불가능)
        if not queue1 or not queue2:
            return -1
        
        if count > 0:
            # 합이 큰 쪽에서 원소를 추출하여 다른 쪽에 추출한 원소 추가
            if sum1 < sum2:
                i = queue2.popleft()
                queue1.append(i)
                sum2 -= i
                sum1 += i
                count -= 1
                answer += 1

            elif sum1 > sum2:
                i = queue1.popleft()
                queue2.append(i)
                sum1 -= i
                sum2 += i
                count -= 1
                answer += 1
        else:
            return -1
            
    return answer