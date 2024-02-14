# 이진 탐색 함수(재귀적 구현)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 중간점

    if array[mid] == target: # target을 찾았으면 리턴
        return mid
    elif array[mid] > target: # target이 중간점보다 작으면 왼쪽부분 탐색
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target: # target이 중간점보다 크면 오른쪽부분 탐색
        return binary_search(array, target, mid+1, end)
    else:
        return None

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
A.sort()

# B의 요소가 A에 있는지 이진탐색으로 찾기
for i in B: 
    result = binary_search(A, i, 0, n-1)
    if result == None: # A에 없으면 0 출력
        print(0)
    else: # A에 있으면 1 출력
        print(1)