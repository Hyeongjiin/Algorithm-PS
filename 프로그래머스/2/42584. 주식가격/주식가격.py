def solution(prices):
    answer = [0] * len(prices)
    stack = [(prices[0], 0)]
    turn = 1
    while stack:
        if prices[turn] >= stack[-1][0]:
            stack.append((prices[turn], turn))
            turn += 1
            if turn == len(prices):
                break
        else:
            down = stack.pop()
            answer[down[1]] = turn - down[1]
            if not stack:
                stack.append((prices[turn], turn))
                turn += 1
                if turn == len(prices):
                    break
    if stack:
        last = stack.pop()
        for i in stack:
            answer[i[1]] = last[1] - i[1]
    return answer