import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# union 연산 함수
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y :
        arr[y] = x

# find 연산 함수
def find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = find(arr[x]) # 재귀 함수를 나오면서 대표 노드로 변경
        return arr[x]

# 같은 집합인지 확인하는 함수
def check(x, y):
    if find(x) == find(y):
        print('YES')
    else:
        print('NO')


n, m = map(int, input().split()) # 원소 개수, 질의 개수

# 처음에는 각 노드가 모두 대표 노드이므로 value를 index로 초기화
arr = [i for i in range(n+1)] 

for i in range(m):
    q, a, b = map(int, input().split())

    # 0이면 union 연산
    if q == 0:
        union(a, b)
    # 1이면 같은 집합에 포함 되어 있는지 확인
    else:
        check(a, b)