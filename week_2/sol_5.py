# 프로그래머스 입국심사
# 1. 최소 0에서 (최대 걸리는 시간) * (인원수) 사이값 계산
# 2. 각 심사관들이 주어진 시간에 심사할 수 있는 인원수 계산
# 3-1. 인원수가 n 값보다 작으면 low = mid + 1
# 3-2. 인원수가 n 값보다 크거나 같으면 high = mid - 1
#      최대값 계산

def binary_search(n, times):
    low = 0
    high = max(times) * n
    mn = high
    
    while low <= high:
        mid = (low+high)//2
        check = 0
        
        for i in range(len(times)):
            check += mid // times[i]
            
        if check < n:
            low = mid + 1
        elif mn <= mid:
            break
        elif mn > mid:
            mn = mid
            high = mid - 1
            
    return mn

def solution(n, times):
    answer = binary_search(n, times)
    return answer