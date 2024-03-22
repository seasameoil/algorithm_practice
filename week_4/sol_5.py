# 백준 2875 대회 or 인턴
import sys

# 1. 여학생 기준으로 팀 구성 먼저하기
# 2. 남학생이 팀에 들어가는거 확인
# 3. 남학생 남으면 인턴으로, 안 남으면 K 확인해서 팀 줄이기

N, M, K = map(int, sys.stdin.readline().split())

woman_team = N//2
man_team = M
woman_remain = N%2
man_remain = 0

if woman_team <= man_team:
    man_remain = M-woman_team
else:
    woman_remain = (woman_team-man_team) * 2
    woman_team = man_team
    man_team = 0

remain = woman_remain + man_remain

if remain >= K:
    print(woman_team)
else:
    while remain < K:
        remain += 3
        woman_team -= 1
    print(woman_team)
