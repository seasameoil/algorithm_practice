# 백준 1260 DBF와 BFS
import sys
from collections import deque

def dfs_deque(start_node):
    visited = []
    need_visited = deque()

    # 시작 노드 설정
    need_visited.append(start_node)

    # 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        # 시작 노드 지정
        node = need_visited.pop()
        # 방문한 리스트에 없다면
        if node not in visited:
            # 방문 리스트에 노드를 추가
            visited.append(node)
            # 인접 노드들을 방문 예정리스트에 추가
            need_visited.extend(reversed(graph[node]))
    return visited

def dfs_recursive(start, visited=[]):
    # 데이터를 추가하는 명령어
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(node, visited)
    return visited

def bfs(start_node):
    visited = list() # 방문한 노드 담는 배열
    need_visited = deque() # 방문 예정인 노드 담는 배열

    need_visited.append(start_node) # 시작 노드 담기

    while need_visited: # 더이상 방문할 노드가 없을 때까지
        node = need_visited.popleft() # 방문할 노드를 앞에서 부터 꺼내기
        
        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited

N, M, V = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점을 작은 것부터 방문하기 위해 오름차순 정렬
for i in range(1, N+1):
    graph[i].sort()

dfs_answer = dfs_deque(V)
# print(dfs_recursive(V))
bfs_answer = bfs(V)

print(" ".join(map(str, dfs_answer)))
print(" ".join(map(str, bfs_answer)))