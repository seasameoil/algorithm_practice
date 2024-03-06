from queue import PriorityQueue
import sys

T = int(sys.stdin.readline().rstrip()) # 테스트 전체의 개수

for _ in range(T):
    # 문서의 개수와 몇 번째로 인쇄되었는지 궁금한 문서
    N, M = map(int, sys.stdin.readline().rstrip().split())
    printer = list(map(int, sys.stdin.readline().rstrip().split()))
    q = PriorityQueue()
    cnt = 0

    if N == 1:
        print(1)
    else:
        # priority queue에 printer 값 넣음
        for value in printer:
            q.put((-value, value))
        find = printer[M]

        while printer:
            x = q.get()[1]
            y = printer.pop(0)
            if x == y:
                if M == 0: break
                else: M -= 1
                cnt += 1
            else:
                printer.append(y)
                q.put((-x, x))
                if M == 0: M = len(printer)-1
                else: M -= 1
        
        print(cnt+1)