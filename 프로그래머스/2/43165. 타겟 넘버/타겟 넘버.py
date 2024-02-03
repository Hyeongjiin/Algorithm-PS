'''
BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    length = len(numbers) - 1
    total = 0
    q.append((total + numbers[0], 0))
    q.append((total - numbers[0], 0))
    while q:
        cur_total, cur_idx = q.popleft()
        if cur_idx == length:
            if cur_total == target:
                answer += 1
            continue
        q.append((cur_total + numbers[cur_idx + 1], cur_idx + 1))
        q.append((cur_total - numbers[cur_idx + 1], cur_idx + 1))

    return answer
'''

#DFS
def solution(numbers, target):
    global answer
    answer = 0
    length = len(numbers) - 1
    dfs(0, -1, numbers, target, length)

    return answer

def dfs(cur_total, cur_idx, numbers, target, length):
    global answer
    if cur_idx == length:
        if cur_total == target:
            answer += 1
        return 
    dfs(cur_total + numbers[cur_idx + 1], cur_idx + 1, numbers, target, length)
    dfs(cur_total - numbers[cur_idx + 1], cur_idx + 1, numbers, target, length)

    
    