import sys

N = int(sys.stdin.readline().rstrip())
coordinate = list(map(int, sys.stdin.readline().rstrip().split()))

check = sorted(list(set(coordinate)))
check_dict = {check[i] : i for i in range(len(check))}
answer = []

for x in coordinate:
    answer.append(str(check_dict[x]))

print(" ".join(answer))