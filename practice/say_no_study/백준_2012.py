# 백준 2012 등수 매기기
import sys

N = int(sys.stdin.readline().rstrip())
scores = [0]

for _ in range(N):
    scores.append(int(sys.stdin.readline().rstrip()))

scores.sort()

answer = 0
for i in range(1, N+1):
    answer += abs(scores[i] - i)

print(answer)