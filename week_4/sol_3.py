# 백준 12845 모두의 마블
import sys

# 1. 값 입력받음
# 2. 가장 큰 값 찾기
# 3. 가장 큰 값 * (n-2) + 전체 값

N = int(sys.stdin.readline().rstrip())
card = list(map(int, sys.stdin.readline().split()))

s = sum(card) + max(card)*(N-2)
print(s)