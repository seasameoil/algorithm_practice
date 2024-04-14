# 백준 1074 Z
import sys

N, r, c = map(int, sys.stdin.readline().split())

def solution(N, r, c):
    half = 2 ** (N-1)

    if N==0:
        return 0

    if r < half and c < half:
        return solution(N-1, r, c)
    elif r < half and c >= half:
        return half**2 + solution(N-1, r, c-half)
    elif r >= half and c < half:
        return 2*half**2 + solution(N-1, r-half, c)
    else:
        return 3*half**2 + solution(N-1, r-half, c-half)
    
print(solution(N, r, c))
