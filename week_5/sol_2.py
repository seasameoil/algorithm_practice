# 백준 1759 암호 만들기
import sys
from itertools import combinations

# 1. permutation 사용
# 2. 한 개의 모음과 두 개의 자음 이상으로 이루어져있는지 확인

L, C = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(str, sys.stdin.readline().split())))
vowels = ['a', 'e', 'i', 'o', 'u']

c_list = list(combinations(numbers, L))

for combination in c_list:
    vowel = sum(1 for char in combination if char in vowels)
    constant = L - vowel
    if vowel >= 1 and constant >= 2:
        print(''.join(combination))