# 백준 1965 - 상자 넣기
import sys

n = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j]+1)
    print(dp)

print(max(dp))