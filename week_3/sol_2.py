# 백준 2667 단지번호 붙이기
import sys
from collections import deque

# 방향 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(house, x, y):
    queue = deque()
    queue.append((x, y))
    house[x][y] = 0
    cnt = 1 # 현재 단지의 수

    while queue:
        x, y = queue.popleft()

        for i in range(4):    
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 넘어감
            if nx < 0 or nx >= N or ny <0 or ny >= N:
                continue

            if house[nx][ny] == 1:
                house[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    
    return cnt

N = int(sys.stdin.readline().rstrip())
house = []
result = []

for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            result.append(bfs(house, i, j))

print(len(result))
result.sort()
for x in result:
    print(x)