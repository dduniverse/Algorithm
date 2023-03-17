def solution(i, j, k):
    nums = ''.join([str(num) for num in range(i, j+1)])
    return nums.count(str(k))