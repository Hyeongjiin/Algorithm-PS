def solution(n, lost, reserve):
    p = [0] * (n + 1)
    for i in reserve:
        p[i] += 1
    for i in lost:
        p[i] -= 1
    answer = 0
    for i in range(1, n + 1):
        if p[i] >= 0:
            answer += 1
        if p[i] == -1:
            if i - 1 > 0 and p[i - 1] > 0:
                p[i - 1] -= 1
                p[i] += 1
                answer += 1
                continue
            if i + 1 < n + 1 and p[i + 1] > 0:
                p[i + 1] -= 1
                p[i] += 1
                answer += 1

    return answer