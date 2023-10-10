def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length    # 다리
    onbridge = sum(bridge)          # 다리 위 트럭 하중
    answer = 0                      # 시간
    
    # 다리 위의 트럭이 없을 때까지(=모든 트럭이 다리를 건널 때 까지)
    while bridge:
        answer += 1
        onbridge -= bridge.pop(0) # 맨 앞에 위치한 트럭이 다리를 지나면 하중 감소
        
        # 남은 트럭이 있으면
        if truck_weights:
            # 다리 위 트럭 총 무게 + 새로운 트럭 <= 견딜 수 있는 무게이면
            if onbridge + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)    # 대기 트럭에서 출발
                bridge.append(new_truck)            # 다리에 새로운 트럭 추가
                onbridge += new_truck               # 새로운 트럭만큼 다리 하중 증가
            
            # 그렇지 않으면
            else:
                bridge.append(0)                    # 다리에 0을 추가해 자리 이동 표시
                    
    return answer