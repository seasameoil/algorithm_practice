# 백준 2512 예산
import sys

N = int(sys.stdin.readline().rstrip())
budgets = sorted(list(map(int, sys.stdin.readline().split())))
budget = int(sys.stdin.readline().rstrip())

low = 0
high = max(budgets)
answer = 0

while low <= high:
    mid = (low+high) // 2

    temp = 0
    for x in budgets:
        if x <= mid:
            temp += x
        else:
            temp += mid
    
    if temp == budget:
        answer = mid
        break
    elif temp < budget:
        answer = max(answer, mid)
        low = mid+1
    else:
        high = mid-1

print(answer)