import sys
input = sys.stdin.readline

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
    
    
    
n = int(input()) # 도시의 수
m = int(input()) # 여행 계획에 있는 도시의 수

# 연결 정보 저장
graph = [[0 for _ in range(n+1)]]
for i in range(n):
    temp = [0]
    temp += list(map(int, input().split()))
    graph.append(temp)
# print(graph)

# 여행 계획
route = [0]
route += list(map(int, input().split()))


# 처음에는 각 노드가 모두 대표 노드이므로 value를 index로 초기화
arr = [i for i in range(n+1)] 

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == 1:
            union(i, j)
# print(arr)

# 연결되는지 확인 = 대표 노드가 같은지 확인
index = find(route[1])    
connect = 1
for i in range(2, len(route)):
    # 같지 않으면 연결되어 있지 않은 것임
    if index != find(route[i]):
        connect = 0
        break
    
if connect:
    print('YES')
else:
    print('NO')