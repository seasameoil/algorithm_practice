import sys
import collections

n = int(sys.stdin.readline().rstrip())
card = sorted(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
want = list(map(int, sys.stdin.readline().rstrip().split()))

answer = []
dict_a = collections.Counter(card)

for i in want:
	if i in dict_a:
		answer.append(dict_a[i])
	else:
		answer.append(0)


print(" ".join(map(str, answer)))