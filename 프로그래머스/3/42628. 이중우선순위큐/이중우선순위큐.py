import heapq

def solution(operations):
    max_q = []
    min_q = []
    used = [0] * len(operations)
    for idx, operation in enumerate(operations):
        operation = operation.split(' ')
        operator = operation[0]
        num = int(operation[1])
        if operator == 'I':
            heapq.heappush(min_q, (num, idx))
            heapq.heappush(max_q, (-num, idx))
        elif operator == 'D':
            if num == 1 and max_q:
                out = heapq.heappop(max_q)
                used[out[1]] = 1
            elif num == -1 and min_q:
                out = heapq.heappop(min_q)
                used[out[1]] = 1
        while max_q and used[max_q[0][1]] == 1:
            heapq.heappop(max_q)
        while min_q and used[min_q[0][1]] == 1:
            heapq.heappop(min_q)             
    answer = []
    if not max_q:
        answer = [0, 0]
    else:
        answer.append(-heapq.heappop(max_q)[0])
        answer.append(heapq.heappop(min_q)[0])
    return answer