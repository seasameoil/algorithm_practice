# 백준 11286 절댓값 힙
import sys, heapq

N = int(sys.stdin.readline().rstrip())
h1, h2 = [], []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x < 0:
        heapq.heappush(h1, (-x, x))
    elif x > 0:
        heapq.heappush(h2, x)
    elif x == 0:
        if not h1 and not h2:
            print(0)
        elif not h1:
            print(heapq.heappop(h2))
        elif not h2:
            print(heapq.heappop(h1)[1])
        else: 
            if h1[0][0] <= h2[0]:
                print(heapq.heappop(h1)[1])
            else:
                print(heapq.heappop(h2))
