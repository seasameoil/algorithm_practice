# 백준 11047 동전0
import sys

# 1. 주어진 동전들 다 저장
# 2. 큰 수부터 돌면서 나눌 수 있는지 확인
#    나눌 수 있으면 몫 = 동전 개수, 나머지 = 계속 계산
# 3. 나머지가 0이 될 때까지 반복

N, K = map(int, sys.stdin.readline().split())
money = []

for _ in range(N):
    money.append(int(sys.stdin.readline().rstrip()))

ans = 0
for i in range(N-1, -1, -1):
    if money[i] <= K:
        ans += K // money[i]
        K %= money[i]

    if K == 0:
        break

print(ans)