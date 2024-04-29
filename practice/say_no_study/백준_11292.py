# 백준 11292 키 큰 사람
import sys

N = int(sys.stdin.readline().rstrip())

while N != 0:
    answer = []
    mx = 0
    for _ in range(N):
        name, height = sys.stdin.readline().split()

        if float(height) > mx:
            mx = float(height)
            if len(answer) > 0:
                answer = []
                answer.append(name)
            else:
                answer.append(name)
        elif float(height) == mx:
            answer.append(name)
    
    print(' '.join(answer))

    N = int(sys.stdin.readline().rstrip())