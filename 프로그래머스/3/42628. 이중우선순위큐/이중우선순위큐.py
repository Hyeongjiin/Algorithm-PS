import heapq

def solution(operations):
    max_q = []
    min_q = []
    count = 0
    for operation in operations:
        operation = operation.split(' ')
        operator = operation[0]
        num = int(operation[1])
        if operator == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            count += 1
        elif operator == 'D':
            if num == 1 and max_q:
                heapq.heappop(max_q)
                count -= 1
            elif num == -1 and min_q:
                heapq.heappop(min_q)
                count -= 1
        if count == 0:
            max_q = []
            min_q = []
    answer = []
    if not max_q:
        answer = [0, 0]
    else:
        answer.append(-heapq.heappop(max_q))
        answer.append(heapq.heappop(min_q))
    return answer