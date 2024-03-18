# 백준 2178 미로탐색
import sys
from collections import deque

# 미로 입력받기
# BFS, 상하좌우로 움직이며 길이 1이면 이동
# 최소길이 측정

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    maze[y][x] = 0 # 방문처리
    distance[y][x] = 1 # 최단 거리 재기

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = 0 # 방문 처리
                distance[ny][nx] = distance[y][x] + 1 # 거리 + 1
                queue.append((ny, nx))
    
    return distance[N-1][M-1]
            


N, M = map(int, sys.stdin.readline().split())
maze = []
distance = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

print(BFS(0, 0))