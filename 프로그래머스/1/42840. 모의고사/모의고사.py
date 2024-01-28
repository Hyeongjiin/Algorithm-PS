def solution(answers):
    result = []
    f = [1, 2, 3, 4, 5] 
    s = [2, 1, 2, 3, 2, 4, 2, 5]
    t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    counts = [0, 0, 0]
    for idx, answer in enumerate(answers):
        if answer == f[idx % len(f)]:
            counts[0] += 1
        if answer == s[idx % len(s)]:
            counts[1] += 1
        if answer == t[idx % len(t)]:
            counts[2] += 1
    max_count = max(counts)
    for i in range(3):
        if counts[i] == max_count:
            result.append(i + 1)
    return result