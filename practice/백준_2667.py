# 다시풀기
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = []
    queue.append((x, y))
    visited[x][y] = True
    cnt = 0

    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False and maps[nx][ny] == '1':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    
    return cnt+1


N = int(sys.stdin.readline().rstrip())
maps = []
visited = [[False for _ in range(N)] for _ in range(N)]
answer = []

for i in range(N):
    maps.append(list(sys.stdin.readline().rstrip()))

for i in range(N):
    for j in range(N):
        if maps[i][j] == '1' and visited[i][j] == False:
            c = BFS(i, j)
            if c > 0:
                answer.append(c)

print(len(answer))
print("\n".join(map(str, sorted(answer))))
