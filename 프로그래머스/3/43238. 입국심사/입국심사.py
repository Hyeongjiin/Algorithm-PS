def solution(n, times):
    start = 1
    end = max(times) * n
    answer = int(10e12)
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