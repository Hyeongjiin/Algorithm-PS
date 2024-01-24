def solution(citations):
    start = 0
    end = max(citations)
    max_citation = 0
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for citation in citations:
            if citation >= mid:
                count += 1
        if count >= mid:
            start = mid + 1
            if mid > max_citation:
                max_citation = mid
        else:
            end = mid - 1
    answer = max_citation
    return answer