def solution(number, k):
    number = list(number)
    number = number[::-1]
    result = []
    count = 0
    while number:
        if count == k:
            break
        plus = number.pop()
        if not result:
            result.append(plus)
        else:
            while result and result[-1] < plus:
                result.pop()
                count += 1
                if count == k:
                    break
            result.append(plus)
    while number:
        result.append(number.pop())
    while count < k:
        result.pop()
        count += 1
    answer = ''.join(result)
    return answer