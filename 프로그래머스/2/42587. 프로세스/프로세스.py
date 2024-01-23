from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    maxi = max(q)[0]

    count = 0
    while q:
        cur = q.popleft()
        if cur[0] < maxi:
            q.append(cur)
        else:
            count += 1
            if cur[1] == location:
                answer = count
                break
            maxi = max(q)[0]
    

    return answer