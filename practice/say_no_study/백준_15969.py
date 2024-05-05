# 백준 15969 행복
import sys

N = int(sys.stdin.readline().rstrip())
students = list(map(int, sys.stdin.readline().split()))

print(max(students) - min(students))