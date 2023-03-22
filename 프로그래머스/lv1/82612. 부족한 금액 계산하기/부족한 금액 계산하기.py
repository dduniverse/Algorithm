def solution(price, money, count):
    sum = 0
    for i in range(count):
        sum += (i+1) * price
        
    if sum < money:
        return 0
    return sum - money