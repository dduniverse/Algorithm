def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2  # 중앙값(=리스트를 나눌 기준점)

    left = merge_sort(arr[:mid]) 
    right = merge_sort(arr[mid:])

    i, j = 0, 0 # left, right 각각의 포인터
    sort = [] # 정렬된 배열
  
   #둘중 하나조건에 부합하지 않을경우 while문 빠져나감 
    while i < len(left) and j < len(right): 
      if left[i] < right[j]:
        sort.append(left[i])
        i+=1
      else:
        sort.append(right[j])
        j+=1

    # 정렬되지 않고 남은 요소 추가
    sort += left[i:] 
    sort += right[j:]

    return sort


# 입력
n = int(input())
num = [int(input()) for _ in range(n)]

# 병합 정렬 함수 호출
result = merge_sort(num)

# 정렬 결과 출력
for i in result:
    print(i)