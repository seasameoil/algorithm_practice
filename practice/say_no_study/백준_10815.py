# 백준 10815 숫자 카드
import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

cards_dict = defaultdict(int)

for c in cards:
    cards_dict[c] = 1

nums = list(map(int, sys.stdin.readline().split()))
answer = []

for x in nums:
    if x in cards_dict:
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))