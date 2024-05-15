# 백준 2805 나무자르기
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)
answer = 0

while low <= high:
    mid = (low + high) // 2

    temp = 0
    for t in trees:
        if t < mid:
            temp += 0
        else:
            temp += (t-mid)
    
    if temp == M:
        answer = mid
        break
    elif temp < M:
        high = mid - 1
    else:
        low = mid + 1
        answer = max(answer, mid)

print(answer)