# 백준 14501 퇴사
import sys

N = int(sys.stdin.readline().rstrip())
days = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    days.append((x, y))

dp = [0 for _ in range(N+1)]

for i in range(N):
    day, money = days[i]
    if i+day < N+1:
        dp[i+day] = max(dp[i+day], max(dp[:i+1]) + money)
print(max(dp))