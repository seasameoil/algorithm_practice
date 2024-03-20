# 백준 11399 ATM
import sys
from collections import deque

# 1. 주어진 값을 입력받기
# 2. 순서대로 정렬
# 3. arr[i+1] = arr[i+1] + arr[i]

N = int(sys.stdin.readline().rstrip())
Q = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(len(Q)-1):
    Q[i+1] += Q[i]

print(sum(Q))