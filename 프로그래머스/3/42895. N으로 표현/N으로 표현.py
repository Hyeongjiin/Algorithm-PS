def solution(N, number):
    answer = -1
    dp = []
    for i in range(1, 9):
        data = set()
        num_cal = int(str(N) * i)
        data.add(num_cal)
        for j in range(0, i - 1):
            for k in dp[j]:
                for h in dp[-j-1]:
                    data.add(k + h)
                    data.add(k - h)
                    data.add(k * h)
                    if h != 0:
                        data.add(k // h)
        if number in data:
            answer = i
            break
        dp.append(data)
    return answer