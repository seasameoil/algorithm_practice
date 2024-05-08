# 백준 28324 스케이트 연습
import sys

N = int(sys.stdin.readline().rstrip())
speeds = list(map(int, sys.stdin.readline().split()))
speeds.reverse()

answer = 0
speed = 0
for x in speeds:
    if x > speed:
        speed += 1
        answer += speed
    elif x <= speed:
        speed = x
        answer += speed
    
print(answer)