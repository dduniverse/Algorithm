import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 노드의 개수

# 트리 정보
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
    
# 전위 순회
def preorder(x):
    if x == '.':
        return
    else:
        print(x, end='') # 현재 노드
        preorder(tree[x][0]) # 왼쪽 노드
        preorder(tree[x][1]) # 오른쪽  노드

# 중위 순회        
def inorder(x):
    if x == '.':
        return
    else:
        inorder(tree[x][0]) # 왼쪽 노드
        print(x, end='') # 현재 노드
        inorder(tree[x][1]) # 오른쪽 노드
        
# 후위 순회
def postorder(x):
    if x == '.':
        return
    else:
        postorder(tree[x][0]) # 왼쪽 노드
        postorder(tree[x][1]) # 오른쪽 노드
        print(x, end='') # 현재 노드

# 출력 - 루트 노드 A
preorder('A')
print()
inorder('A')
print()
postorder('A')