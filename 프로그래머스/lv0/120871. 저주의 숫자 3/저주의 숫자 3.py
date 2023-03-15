def solution(n):
    answer = 0
    for i in range(1, n+1): # n의 3x숫자를 알기 위해 1부터 n까지의 수를 탐색
        answer += 1
        while ('3' in str(answer)) or (answer % 3 == 0): # 3이 포함되어 있거나 3의 배수이면 +1을 해줌
            answer += 1
    return answer