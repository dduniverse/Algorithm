import sys
input = sys.stdin.readline

n = int(input()) # 노드 개수
graph = []
for _ in range(n):
    graph.append(list(input()))

edges = [] # 에지 리스트
total = 0 # 전체 길이
for i in range(n):
    for j in range(n):
        # 소문자일때 길이
        if graph[i][j].islower():
            weight = ord(graph[i][j]) - ord('a') + 1
        # 대문자일때 길이
        elif graph[i][j].isupper():
            weight = ord(graph[i][j]) - ord('A') + 27
        # 영어가 아닐때(= 0일 때)
        else:
            weight = int(graph[i][j])
        
        total += weight
        # 서로 다른 컴퓨터에 연결(!=0)된 경우
        if i != j and weight != 0:
            edges.append((i, j, weight))
        

edges.sort(key=lambda x: x[2]) # 가중치 기준 오름차순 정렬

arr = [i for i in range(n)] # 유니온 파인드 리스트

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        arr[y] = x
        
def find(x):
    if x == arr[x]:
        return x
    else:
        arr[x] = find(arr[x])
        return arr[x]

edge, weights = 0, 0
for s, e, w in edges:
    if find(s) != find(e):
        union(s, e)
        edge += 1
        weights += w
                 
# 기부할 수 있는 길이 = 전체 - 최소신장트리
if edge == n-1:
    print(total - weights)
else:
    print(-1)