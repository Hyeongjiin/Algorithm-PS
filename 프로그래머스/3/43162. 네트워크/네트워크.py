# BFS
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            bfs(computers, visited, i)
    return answer

def bfs(computers, visited, node):
    q = deque()
    q.append(node)
    visited[node] = True
    while q:
        cur_node = q.popleft()
        for node, val in enumerate(computers[cur_node]):
            if val == 1 and visited[node] == False:
                visited[node] = True
                q.append(node)

"""
DFS
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            dfs(computers, visited, i)
    return answer

def dfs(computers, visited, cur_node):
    visited[cur_node] = True
    for node, val in enumerate(computers[cur_node]):
        if val == 1 and visited[node] == False:
            dfs(computers, visited, node)
"""