# 백준 30970 선택의 기로
import sys

N = int(sys.stdin.readline().rstrip())
miniature = []

for _ in range(N):
    Q, P = map(int, sys.stdin.readline().split())
    miniature.append((Q, P))

miniature.sort(key= lambda x :(-x[0], x[1]))
print(miniature[0][0], miniature[0][1], miniature[1][0], miniature[1][1])
miniature.sort(key= lambda x :(x[1], -x[0]))
print(miniature[0][0], miniature[0][1], miniature[1][0], miniature[1][1])