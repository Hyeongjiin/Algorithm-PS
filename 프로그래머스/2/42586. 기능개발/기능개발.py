from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(speeds)):
        days = math.ceil((100 - progresses[i]) / speeds[i])
        q.append(days)
    start = q[0]
    count = 0
    print(q)
    while q:
        compare = q.popleft()
        if compare <= start:
            count += 1
        else:
            start = compare
            answer.append(count)
            count = 1
    if count != 0:
        answer.append(count)
    return answer