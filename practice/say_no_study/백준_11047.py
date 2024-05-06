# 백준 11047 동전 0
import sys

N, K = map(int, sys.stdin.readline().split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

answer = 0 
for i in range(N-1, -1, -1):
    if K >= coins[i]:
        answer += (K//coins[i])
        K %= coins[i]

print(answer)