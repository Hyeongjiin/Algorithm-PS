def solution(n, times):
    times.sort()
    start = 1
    end = times[-1] * n
    answer = int(10e19)
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in times:
            count += mid // time
        if count < n:
            start = mid + 1
        elif count >= n:
            end = mid - 1
            answer = min(answer, mid)
    return answer