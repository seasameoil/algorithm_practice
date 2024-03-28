# 백준 2661 좋은 수열
import sys

# 1. 노드 선택 시 가장 작은 노드 선택
# 2. 중복되는 문자열 있는지 확인

sys.setrecursionlimit(100000)

def check_pattern(s, node):
    new_str = s + node
    for i in range(1, len(new_str)//2 +1):
        pattern = new_str[-i*2:-i]
        last_pattern = new_str[-i:]

        if pattern == last_pattern:
            return True
    
    return False

def DFS(ans):
    if len(ans) == N:
        print(ans)
        sys.exit(0)
    
    for node in nodes:
        if not check_pattern(ans, node):
            DFS(ans+node)
            
             
ans = "1"

N = int(sys.stdin.readline().rstrip())
nodes = ['1', '2', '3']

DFS("1")
