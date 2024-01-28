def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            count = i * 2 + (yellow // i) * 2 + 4
            if count == brown:
                answer.append(yellow // i + 2)
                answer.append(i + 2)
                break
    return answer