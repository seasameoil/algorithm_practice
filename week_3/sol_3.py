# 백준 1012 유기농배추
import sys
from collections import deque

# 1. 각 테스트 케이스의 배열 가로 길이, 세로 길이, 위치의 개수를 저장
# 2. 입력받은 좌표 위치를 1로 설정
# 3. 배열에 대하여 BFS 진행

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def BFS(farm, y, x):
    queue = deque()
    queue.append((y, x))
    farm[y][x] == 0 # 방문처리

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= M or 0 > ny or ny >= N:
                continue
            if farm[ny][nx] == 1:
                farm[ny][nx] = 0
                queue.append((ny, nx))

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    farm = [[0 for _ in range(M)] for _ in range(N)] # 밭 생성
    for _ in range(K):
        y, x = map(int, sys.stdin.readline().rstrip().split())
        farm[x][y] = 1
    
    cnt = 0
    for j in range(N):
        for i in range(M):
            if farm[j][i] == 1:
                BFS(farm, j, i)
                cnt += 1
    print(cnt)
    
