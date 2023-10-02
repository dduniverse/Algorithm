def solution(order):
    stack = []  # 보조 컨테이터
    now = 0     # 택배 기사님이 원하는 순서대로 작업하기 위한 order 접근용 변수
    answer = 0  # 실을 수 있는 상자 개수
    
    # 1번부터 순서대로 진행되는 컨테이너 벨트
    for i in range(1, len(order)+1):
        stack.append(i) # 일단, 보조 컨테이터에 옮김
        
        # 보조 컨테이터의 마지막 상자가 order와 같으면
        while stack and stack[-1] == order[now]:
            answer += 1
            stack.pop() # 보조 컨테이너에서 out
            now += 1    # 다음 상자 작업
                
    return answer
                