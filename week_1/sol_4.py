import sys

n = sys.stdin.readline().rstrip()

for _ in range(int(n)):
    text = sys.stdin.readline().rstrip()
    s = []
    flag = True

    for i in text:
        if i == "(":
            s.append("(")
        elif i == ")" and len(s) == 0:
            flag = False
            break
        else:
            s.pop()
    
    if len(s) != 0:
        print("NO")
    elif len(s) == 0 and not flag:
        print("NO")
    else:
        print("YES")