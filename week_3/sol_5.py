# 백준 1697 숨바꼭질
import sys
from collections import deque

# 1. 각 트리의 자식 노드를 X-1, X+1, 2*X 생성
# 2. 각 노드 중 가장 먼저 K의 값 도달하는 깊이 측정 (BFS)

def bfs(depth, k):
    queue = deque()
    visited = set([N])

    # 처음 root 노드 설정
    queue.append((0, N))

    while queue:
        depth, current = queue.popleft()
        
        if current == k:
            return depth
        
        # 이동할 수 있는 방향 계산
        children = [current-1, current+1, current*2]

        for child in children:
            if child not in visited and 0 <= child <= 100000:
                visited.add(child)
                queue.append((depth+1, child))


N, K = map(int, sys.stdin.readline().split())

print(bfs(0, K))