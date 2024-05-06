#백준 1010 다리놓기
import sys
from math import factorial

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(factorial(M) // (factorial(M-N) * factorial(N)))