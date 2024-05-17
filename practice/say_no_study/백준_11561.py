# 백준 11561 징검다리
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x = int(sys.stdin.readline().rstrip())

    low = 0
    high = x
    answer = 0

    while low <= high:
        mid = (low + high) // 2

        s = mid * (mid+1) // 2
        if s == x:
            answer = mid
            break
        elif s < x:
            if s + (mid+1) > x:
                answer = mid
                break
            else:
                low = mid+1
        else:
            high = mid-1
    print(answer)