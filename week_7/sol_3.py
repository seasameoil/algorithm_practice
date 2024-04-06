# 백준 2696 중앙값 구하기
import sys
from queue import PriorityQueue

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    M = int(sys.stdin.readline().rstrip())
    numbers = []
    if M > 10:
        for _ in range((M + 9) // 10):
            numbers.extend(list(map(int, sys.stdin.readline().split())))
    else:
        numbers = list(map(int, sys.stdin.readline().split()))
    
    _numbers = []
    answer = []
    for i, x in enumerate(numbers):
        _numbers.append(x)
        _numbers.sort()
        if (i+1)%2 !=0:
            answer.append(_numbers[i//2])
    
    print(len(answer)) # 중앙값의 개수 출력
    for i in range(len(answer)):
        if i > 0 and i % 10 == 0:  # 10개 단위로 줄바꿈
            print()
        print(answer[i], end=' ')
    print()

