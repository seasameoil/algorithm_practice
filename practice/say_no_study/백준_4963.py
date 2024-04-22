import sys
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def BFS(maps, x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = 0
                    cnt += 1
    return cnt


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    maps = []
    for _ in range(h):
        maps.append(list(map(int, sys.stdin.readline().split())))
    
    answer = 0
    # print(maps)
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                if BFS(maps, i, j) > 0:
                    answer += 1
    
    print(answer)
