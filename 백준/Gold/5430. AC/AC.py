from collections import deque
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    p = input()                     # 수행할 함수
    n = int(input())                # 수의 개수
    queue = deque(input()[1:-2].split(','))  # n개의 정수 배열
    r_count = 0

    if n == 0:   # deque는 [''] 의 길이를 0이 아닌 1로 취급하기 때문에 빈 배열로 초기화
        queue = []

    for i in range(len(p)):
        if p[i] == 'R':             # 뒤집기 연산
            r_count += 1
        elif p[i] == 'D':           # 삭제 연산
            if len(queue) == 0:     # 배열이 비어있으면 에러
                print('error')
                break
            else:        # 배열이 비어있지 않은 경우만 삭제 연산 수행
                if r_count % 2 == 0: 
                    queue.popleft()
                else: # R의 개수가 홀수이면 뒤집어진 상태에서 pop 연산
                    queue.pop()

    # break를 만나지 않고 for문이 종료되었을 경우
    else:
        if r_count % 2 == 1:    # R의 개수가 홀수이면 뒤집어줌
            queue.reverse()
        
        print('[' + ','.join(queue) + ']')
