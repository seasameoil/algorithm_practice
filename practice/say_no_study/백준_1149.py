#백준 1149 RGB거리
import sys

N = int(sys.stdin.readline().rstrip())
houses = [[] for _ in range(N)]
answer = float('inf')

for i in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    houses[i].append(R)
    houses[i].append(G)
    houses[i].append(B)

money = 0
dp = [[0 for _ in range(3)] for _ in range(N)]

dp[0][0] = houses[0][0]
dp[0][1] = houses[0][1]
dp[0][2] = houses[0][2]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = houses[i][j] + min(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = houses[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])
        else:
            dp[i][j] = houses[i][j] + min(dp[i-1][j-2], dp[i-1][j-1])

print(min(dp[-1]))