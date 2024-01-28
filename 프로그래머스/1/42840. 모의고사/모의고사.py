import math

def solution(answers):
    answer = []
    length = len(answers)
    f = [1, 2, 3, 4, 5] * math.ceil(length / 5)
    s = [2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(length / 8)
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(length / 10)
    counts = [0, 0, 0]

    for i in range(len(answers)):
        if f[i] == answers[i]:
            counts[0] += 1
        if s[i] == answers[i]:
            counts[1] += 1
        if t[i] == answers[i]:
            counts[2] += 1
    max_count = max(counts)
    for i in range(3):
        if counts[i] == max_count:
            answer.append(i + 1)
    return answer