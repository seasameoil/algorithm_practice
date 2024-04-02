# 백준 11279 최대 힙
import sys, heapq

N = int(sys.stdin.readline().rstrip())
h = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 0 and h:
        print(heapq.heappop(h)[1])
    elif x == 0 and not h:
        print(0)
    else:
        heapq.heappush(h, (-x, x))
