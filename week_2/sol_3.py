import sys

def binary_search(height):
    low = 0
    high = height
    # '적어도 M'의 높이만큼이기 때문에, 최대한 이에 맞추되 M보다 클 수도 있음
    max = 0

    while low <= high:
        mid = (low + high) // 2
        target = 0

        for i in range(len(tree)):
            # 날의 높이가 나무의 길이보다 길 경우 자르지 않음
            if tree[i] < mid:
                continue
            else:
                target += tree[i] - mid

        if M == target:
            max = mid
            return max
        elif M > target:
            high = mid-1
        else:
            low = mid+1
            max = mid
    
    return max

N, M = map(int, sys.stdin.readline().rstrip().split())
tree = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

answer = binary_search(tree[-1]+1)

if answer:
    print(answer)
else:
    print(0)