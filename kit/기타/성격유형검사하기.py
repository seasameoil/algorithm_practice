def solution(survey, choices):
    
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i, s in enumerate(survey):
        point = choices[i] - 4
        
        if point < 0:
            score[s[0]] += abs(point)
        elif point > 0:
            score[s[1]] += abs(point)
    
    types = ['RT', 'CF', 'JM', 'AN']
    answer = ''.join([t[0] if score[t[0]] >= score[t[1]] else t[1] for t in types])
    return answer