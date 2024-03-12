#백준 1654 랜선 자르기
import sys

# 1. K와 N의 값 받아오기
# 2. 주어진 K개의 값 받아오기
# 3. 최소 0에서 주어진 값 중 가장 큰 값 사이의 숫자로 랜선의 길이 결정
# 4. mid로 만들수 있는 랜선의 수 구하기
# 4-1. 랜선의 수가 N 보다 작다면 high = mid - 1
# 4-2. 랜선의 수가 N과 같거나 크다면 low = mid + 1
#      최대값 저장
# 5. 랜선의 길이가 최대값보다 작아지면 계산 멈춤

def binary_search():
    low = 0
    high = max(line)
    mx = 0

    while low<=high:
        mid = (low+high) // 2
        check = 0

        if mid == 0:
            mid += 1

        for i in range(K):
            check += line[i] // mid

        if check < N:
            high = mid - 1
        elif mx < mid:
            mx = mid
            low = mid + 1
    
    return mx



K, N = map(int, sys.stdin.readline().rstrip().split())
line = []

for _ in range(K):
    line.append(int(sys.stdin.readline().rstrip()))

print(binary_search())