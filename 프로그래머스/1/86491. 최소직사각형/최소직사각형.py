def solution(sizes):
    max_w = 0
    max_l = 0
    for size in sizes:
        max_w = max(max_w, max(size))
        max_l = max(max_l, min(size))
    answer = max_w * max_l
    return answer