import sys

def binary_search(target):
    high = len(num_list)-1
    low = 0

    while low <= high:
        mid = (high+low) // 2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] < target:
            low = mid+1
        else:
            high = mid-1
            
    return -1

N = int(sys.stdin.readline().rstrip())
num_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
check_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(len(check_list)):
    if binary_search(check_list[i]) != -1:
        print(1)
    else:
        print(0)