# 백준 1931 회의실 배정
import sys

# 1. 받아서 배열에 튜플로 저장
# 2. 가장 빨리 끝나는 시간 선택
# 3. 카운트 + 1

N = int(sys.stdin.readline().rstrip())
time = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    time.append((x, y))

time_sorted = sorted(time, key=lambda x:(x[1], x[0]))

end_time = time_sorted[0][1]
cnt = 1

for i in range(1, N):
    if time_sorted[i][0] >= end_time:
        end_time = time_sorted[i][1]
        cnt += 1

print(cnt)
