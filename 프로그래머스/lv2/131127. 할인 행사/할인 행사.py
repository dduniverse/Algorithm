def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        discount_list = discount[i:i+sum(number)]
        flag = [True] * len(want)
        for w in range(len(want)):
            if number[w] != discount_list.count(want[w]):
                flag[w] = False
        if all(flag):
            answer += 1
    return answer