# 백준 2579 계단 오르기
import sys

N = int(sys.stdin.readline().rstrip())

steps = [0]
for _ in range(N):
    steps.append(int(sys.stdin.readline().rstrip()))

dp = [0] * (N+1)
dp[1] = steps[1]

if N > 1:
    dp[2] = dp[1] + steps[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2]+steps[i], steps[i]+steps[i-1]+dp[i-3])

print(dp[N])