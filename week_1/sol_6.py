import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    text = list(sys.stdin.readline().rstrip().split())
    answer = []

    for x in text:
        answer.append(x[::-1])
    
    print(" ".join(answer))