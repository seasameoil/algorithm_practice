import sys

# 값 입력 받기
n, k = map(int, sys.stdin.readline().rstrip().split())

# 인원 생성
arr = [i for i in range(1, n+1)]
result = []

idx = 0
# 출력
while arr:
    idx += k-1
    if idx >= len(arr):
        idx %= len(arr)
    result.append(arr.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")