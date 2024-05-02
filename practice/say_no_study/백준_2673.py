# 백준 2573 빙산
import sys
from collections import deque

sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def melt():
    melt_list = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if ice[y][x] > 0:
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= nx < M and 0 <= ny < N and ice[ny][nx] == 0:
                        melt_list[y][x] += 1
    for y in range(N):
        for x in range(M):
            ice[y][x] = max(0, ice[y][x] - melt_list[y][x])

def DFS(x, y):      
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if visited[x][y] == 1:
        visited[x][y] = 0
        DFS(x - 1, y)
        DFS(x, y - 1)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True
    return False


N, M = map(int, sys.stdin.readline().split())
ice = []

for _ in range(N):
    ice.append(list(map(int, sys.stdin.readline().split())))

year = 0
cnt = 0
visited = [[0] * M for _ in range(N)]

def ice_cnt():    # 빙하 덩어리 수를 출력하기 위한 함수

    melt()  # 빙하를 녹임

    tmp = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j]:
                visited[i][j] = 1

    for i in range(N):
        for j in range(M):
            if DFS(i, j):
                tmp += 1    
                
    return tmp


ans = ice_cnt()
group = 1
while True:
    if all(ice[i][j] == 0 for i in range(N) for j in range(M)):
        print(0)
        break

    if ans >= 2:
        print(group)
        break

    else:
        ans = ice_cnt()
        group += 1