def solution(prices):
	# 필요한 개수만큼 0 저장
    answer = [0 for _ in range(len(prices))]
	# 현재 검사하고자 하는 인덱스의 위치 저장용 변수
    cnt = 0
    # prices.pop(0) 의 경우 배열을 한 칸씩 당겨오기 때문에 뒤집어줌
    # -> 시간복잡도 O(N)
    prices.reverse()
    
    while prices:
        # 현재 인덱스 (cnt) 이후에 떨어지는지 검사
        for i in range(len(prices)-2, -1, -1):
            if prices[i] >= prices[-1]:
                answer[cnt] += 1
            else:
                # 본인의 것도 1초로 인정하기 때문에 1 더함
                answer[cnt] += 1
                break
        # 검사 완료한 것은 제거
        prices.pop()
        cnt += 1
            
    return answer