def solution(numbers, hand):
    key = {1: [0, 0],
           2: [0, 1],
           3: [0, 2],
           4: [1, 0],
           5: [1, 1],
           6: [1, 2],
           7: [2, 0],
           8: [2, 1], 
           9: [2, 2],
           0: [3, 1],
           '*': [3, 0],
           '#': [3, 2]
          } # 각 키의 좌표
    
    left, right = key['*'], key['#']
    result = ''
    for i in numbers:
        if i in [1, 4, 7]:
            result += 'L'
            left = key[i]
        elif i in [3, 6, 9]:
            result += 'R'
            right = key[i]
        else:
            num = key[i]
            ll = abs(left[0] - num[0]) + abs(left[1] - num[1])
            rr = abs(right[0] - num[0]) + abs(right[1] - num[1])
            if ll == rr:
                if hand == 'left':
                    left = key[i]
                    result += 'L'
                else:
                    right = key[i]
                    result += 'R'
            elif ll < rr:
                left = key[i]
                result += 'L'
            else:
                right = key[i]
                result += 'R'
    
    return result
            