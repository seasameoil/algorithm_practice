#백준 2231 분해합
import sys

def check_sum(number):
    return number + sum(map(int, str(number)))

N = int(sys.stdin.readline().rstrip())

for i in range(1, N + 1):
    if check_sum(i) == N:
        print(i)
        break
else:
    print(0)
