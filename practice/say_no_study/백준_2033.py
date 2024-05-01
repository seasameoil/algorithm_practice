# 백준 2033 반올림
import sys

N = int(sys.stdin.readline().rstrip())

round_factor = 10
while N >= round_factor:
    if (N % round_factor) >= (round_factor // 2):
        N = ((N // round_factor) + 1) * round_factor
    else:
        N = (N // round_factor) * round_factor
    round_factor *= 10

print(N)