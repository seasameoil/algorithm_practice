# 백준 1182 부분수열의 합
import sys

sys.setrecursionlimit(100000)

# 1. 배열 정렬
# 2. DFS
def DFS(numbers, visited, depth):
    global cnt
    if visited and sum(visited) == M:
        cnt += 1
    
    for i in range(depth, N):
        visited.append(numbers[i])
        DFS(numbers, visited, i+1)
        visited.pop()
        
N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

cnt = 0
DFS(numbers, [], 0)
    
print(cnt)