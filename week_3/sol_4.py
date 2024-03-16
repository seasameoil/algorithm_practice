# 백준 11724 연결 요소의 개수
import sys
from collections import deque

# 재귀 에러 막음
sys.setrecursionlimit(100000)

def dfs(v):
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            dfs(node)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)] # 입력 받기 위한 2차원 배열 생성
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# 호출 횟수
cnt = 0

for i in range(1, N+1):
    # 아직 방문하지 않았다면
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)