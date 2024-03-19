# 백준 7576 토마토
import sys
from collections import deque
from itertools import chain

# 1. 상하좌우의 값 +1로 변경
# 2. 0이 배열 안에 있으면 -1 출력
#    하루만에 익으면 0 출력 (다 익어있던 상태)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()

    # 1이 위치한 곳 모두 찾아 큐에 저장
    for j in range(N):
        for i in range(M):
            if tomato[j][i] == 1:
                queue.append((j, i))

    # BFS 실행하며 익는데 며칠 걸리는지 확인
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 > nx or nx >= M or ny < 0 or ny >= N:
                continue

            if tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1 # 방문표시
                queue.append((ny, nx))

M, N = map(int, sys.stdin.readline().split())

tomato = []

for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

bfs()

if 0 in chain(*tomato):
    print(-1)
elif max(map(max, tomato)) == 1:
    print(0)
else:
    print(max(map(max, tomato))-1)