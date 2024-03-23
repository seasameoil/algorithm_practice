# 백준 10610 30
import sys

# 0. 숫자에 0이 들어있는지 확인
# 1. 숫자들을 다 더해서 3으로 나누어지는지 확인
# 2. 숫자에 0이 없거나 3의 배수가 아니면 -1 출력
# 3. 가장 큰 수 만들기

number = list(map(int, sys.stdin.readline().rstrip()))

s = 0
flag = False
for x in number:
    if x == 0:
        flag = True
    s += x

if s%3 != 0 or flag == False:
    print(-1)
else:
    number.sort(reverse=True)
    print(''.join(map(str, number)))
