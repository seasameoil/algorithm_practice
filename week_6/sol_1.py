# 백준 12026 BOJ 거리
import sys
input = sys.stdin.readline

N = int(input())
walkstreet = input().rstrip()

dp = [float('inf')]*N
dp[0] = 0
for i in range(1,N):
    for j in range(i):
        if walkstreet[j]=='B' and walkstreet[i]=='O':
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))
        elif walkstreet[j]=='O' and walkstreet[i]=="J":
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))
        elif walkstreet[j]=='J' and walkstreet[i]=='B':
            dp[i] = min(dp[i],dp[j]+ pow(i-j,2))

print(dp)
if dp[N-1] != float('inf'):
    print(dp[N-1])
else:
    print(-1)