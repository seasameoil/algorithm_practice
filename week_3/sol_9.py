# 백준 2606 바이러스
import sys

# 1. 딕셔너리 형식으로 연결된 각 정점들 저장
# 2. 1번에서 시작해서 DFS 시작 -> 카운팅을 통한 개수 찾기

sys.setrecursionlimit(100000)

def DFS(v):
    global cnt
    visited[v] = True

    for node in computer[v]:
        if not visited[node]:
            cnt += 1
            DFS(node)

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

computer = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt = 0

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    computer[x].append(y)
    computer[y].append(x)

DFS(1)
print(cnt)