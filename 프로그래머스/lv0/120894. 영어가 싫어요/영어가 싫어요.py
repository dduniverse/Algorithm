def solution(numbers):
    nums = ['zero','one','two','three','four','five',
        'six','seven','eight','nine']
    for i,n in enumerate(nums):
        numbers = numbers.replace(n, str(i))
        
    answer = int(numbers)
    return answer