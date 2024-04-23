# 백준 1389 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

def BFS(graph, start, find):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()
        if current_node == find:
            return len(path)-1
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path+[neighbor]))
    
    return None
    

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

mn = float('inf')
answer = float('inf')
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i != j:
            cnt += DFS(graph, i, j)
    if cnt < mn:
        mn = cnt
        answer = i

print(answer)