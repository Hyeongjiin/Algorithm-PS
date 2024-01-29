import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        low1 = heapq.heappop(scoville)
        low2 = heapq.heappop(scoville)
        heapq.heappush(scoville, low1 + low2 * 2)
        answer += 1
    return answer