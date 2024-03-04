import sys

# 갯수 입력받기
n = int(sys.stdin.readline())
l = []

# 입력 값에 맞추어 배열 정리
for i in range(n):
    text = sys.stdin.readline().rstrip()
    if text == "top":
        if len(l) == 0:
            print(-1)
            continue
        print(l[-1])
    elif text == "pop":
        if len(l) == 0:
            print(-1)
            continue
        print(l.pop())
    elif text == "size":
        print(len(l))
    elif text == "empty":
        if len(l) == 0:
            print(1)
            continue
        print(0)
    else:
        l.append(text[5:])