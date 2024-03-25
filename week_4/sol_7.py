# 백준 1783 병든 나이트
import sys

# 1. 이동횟수가 4번보다 작은 경우
# 1-1. M <= 7, N <= 3
# 2. 이동횟수가 4번보다 많은 경우 (일반적인 경우)

N, M = map(int, sys.stdin.readline().split())

if N==1:
    print(1)
elif N==2:
    print(min(4, (M-1)//2+1))
elif M < 7:
    print(min(4, M))
else:
    print(M-2)