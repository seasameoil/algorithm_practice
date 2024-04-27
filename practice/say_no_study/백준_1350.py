# 백준 1350 진짜 공간
import sys
from math import ceil

N = int(sys.stdin.readline().rstrip())
_file = list(map(int, sys.stdin.readline().split()))
cluster_size = int(sys.stdin.readline().rstrip())

answer = 0
for x in _file:
    if x == 0:
        answer += 0
    else:
        cnt = ceil(x / cluster_size)
        answer += cluster_size * cnt

print(answer)