# 백준 9095 1, 2, 3 더하기
import sys

def count(num):

    if num <= 3:
        return [0, 1, 2, 4][num]

    dp = [0] * (num+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, num+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    return dp[num]

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    print(count(int(sys.stdin.readline().rstrip())))