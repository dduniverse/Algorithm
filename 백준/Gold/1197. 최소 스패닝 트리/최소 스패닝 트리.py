# 왜 index error가 발생할까...
import sys
input = sys.stdin.readline

v, e = map(int, input().split())  # 노드 개수, 간선 개수

edges = []  # 에지 리스트
for _ in range(e):
    a, b, c = map(int, input().split())  # a와 b가 가중치 c인 간선으로 이어져있다.
    edges.append((a, b, c))
    
edges.sort(key=lambda x: x[2]) # 가중치 기준 오름차순 정렬

arr = [i for i in range(v+1)]  # 유니온 파인드 리스트 초기화(index=value)

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

# 총 에지 수, 가중치 합
edge, weight = 0, 0

# edge가 n-1개일 때까지만 실행
while edge < v-1:
    for a, b, c in edges:
        # find 연산의 값이 같으면 두 노드를 연결했을 때 사이클이 형성되는 것
        if find(a) == find(b):
            continue
        else:
            union(a, b)
            edge += 1
            weight += c
            
print(weight)