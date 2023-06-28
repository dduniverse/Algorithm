def solution(progresses, speeds):
    answer = []
    while progresses:
        release = 0 # 배포 개수
        
        # 첫 번째 작업이 100 이상이면 배포+1, 작업 목록에서 제거
        while progresses and progresses[0] >= 100:
            release += 1
            progresses.pop(0)
            speeds.pop(0)
        
        # 계속해서 작업
        progresses = [p+s for p, s in zip(progresses, speeds)]
        
        # 배포할 작업이 있으면
        if release > 0:
            answer.append(release)
            
    return answer