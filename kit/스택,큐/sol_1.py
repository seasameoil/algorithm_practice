import math

def solution(progresses, speeds):
    answer = []
    time_list = [0 for _ in range(len(progresses))]
    
    for i in range(len(progresses)):
        time_list[i] = math.ceil((100 - progresses[i]) / speeds[i])
    
    time_list.reverse()
    print(time_list)
    cnt = 1
    mx = time_list.pop()
    
    while time_list:
        x = time_list.pop()
        if mx < x:
            mx = x
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
            
    answer.append(cnt)
    return answer