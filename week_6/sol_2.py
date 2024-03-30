# 백준 15486 퇴사2
import sys

N = int(sys.stdin.readline().rstrip())
consulting = []

for i in range(N):
    t, m = map(int, sys.stdin.readline().split())
    consulting.append((t, m))

dp = [0 for _ in range(N+1)]

for i in range(N):
    time, money = consulting[i]
    if i+time <= N:
        dp[i+time] = max(dp[i+time], dp[i]+money)
    dp[i+1] = max(dp[i+1], dp[i])
        
print(max(dp))