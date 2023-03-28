def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b').zfill(n)
        arr2[i] = format(arr2[i], 'b').zfill(n)
        
        temp = ''
        for a, b in zip(arr1[i], arr2[i]):
            if a == '0' and b == '0':
                temp += ' '
            if a == '1' or b == '1':
                temp += '#'
        answer.append(temp)
        
    return answer