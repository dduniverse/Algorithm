def solution(ingredient):
    # 1: 빵, 2: 야채, 3: 고기, 1: 빵
    answer = 0
    temp = []
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1, 2, 3, 1]:
            answer += 1
            del temp[-4:]

    return answer