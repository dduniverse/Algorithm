import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

# 그래프 정보
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
start, end = map(int, input().split()) # 출발점, 도착점
    
D = [sys.maxsize for _ in range(n+1)] # 최단 거리 배열 - 최댓값으로 초기화
visit = [0 for _ in range(n+1)] # 방문 배열
queue = PriorityQueue() # 우선순위큐

queue.put((0, start)) # (거리, 노드번호) -> 거리 기준으로 자동 정렬
D[start] = 0 # 출발 노드는 0으로 설정

# 다익스트라
while queue.qsize() > 0:
    # 큐에서 노드를 하나 가져옴
    now = queue.get()
    next = now[1] # 연결 노드 번호
    
    if visit[next] == 1: # 이미 방문했으면 continue
        continue
    else:
        # 방문하지 않은 노드이면
        visit[next] = 1 # 방문 처리
        # 인접 리스트들의 거리 업데이트
        for node, weight in graph[next]:
            if D[next] + weight < D[node]:
                D[node] = D[next] + weight
                queue.put((D[node], node))

# start에서 end로 가는 최단거리 출력
print(D[end])