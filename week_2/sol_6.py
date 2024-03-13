# 숫자 카드
import sys

# 1. 상근이가 가지고 있는 숫자 카드 리스트 생성 (정렬)
# 2. 정수 배열 생성
# 3. 정수 값 확인하면서 상근이가 가지고 있는지 확인 (이분탐색)

def binary_search(target):
    low = 0
    high = N-1

    while low <= high:
        mid = (low+high) // 2

        if num_list[mid] == target:
            return 1
        elif num_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 0


N = int(sys.stdin.readline().rstrip())
num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
check_list = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []

for i in range(M):
    answer.append(str(binary_search(check_list[i])))

print(" ".join(answer))