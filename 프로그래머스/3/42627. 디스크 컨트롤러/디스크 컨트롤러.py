from collections import deque
import heapq

def solution(jobs):
    total_reqs = len(jobs)
    jobs.sort()
    jobs = deque(jobs)
    q = []
    cur_time = jobs[0][0]
    req_time = 0
    while jobs:
        while jobs and jobs[0][0] <= cur_time:
            req = jobs.popleft()
            heapq.heappush(q, (req[1], req[0]))
        if q:
            cur_job = heapq.heappop(q)
            req_time += cur_job[0] + cur_time - cur_job[1]
            cur_time += cur_job[0]
        else:
            cur_time = jobs[0][0]
            
    while q:
        cur_job = heapq.heappop(q)
        req_time += cur_job[0] + cur_time - cur_job[1]
        cur_time += cur_job[0]
    answer = req_time // total_reqs
    return answer