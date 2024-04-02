# 백준 15989 1, 2, 3 더하기 4
import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    M = int(sys.stdin.readline().rstrip())

    dp = [1] * (M+1)
    
    for i in range(2, M+1):
        dp[i] += dp[i-2]
    for i in range(3, M+1):
        dp[i] += dp[i-3]
    
    print(dp[M])