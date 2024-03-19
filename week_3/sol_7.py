# 백준 6603 로또
import sys

def combination(arr, n):
    result = []

    # 0개의 값을 추출하면 빈 배열값 리턴
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        E = arr[i] # 원소 하나 뽑기
        rest_arr = arr[i+1:] # 그 외의 나머지 원소들로 구성된 배열

        # 추가적인 원소 뽑기 (n개를 채울 때까지)
        for e in combination(rest_arr, n-1):
            result.append([E] + e)

    return result

while True:
    l = list(map(int, sys.stdin.readline().split()))
    lotto = l[1:]

    # 0을 입력받을 때까지 while문 돌림
    if l[0] == 0:
        break

    result = combination(lotto, 6)

    # 함수는 2차원 배열로 제공됨
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end = " ")
        print()
    print()