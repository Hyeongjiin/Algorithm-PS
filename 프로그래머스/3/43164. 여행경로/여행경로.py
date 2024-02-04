ways = {}
visited =  {}
answer = []

def solution(tickets):
    for ticket in tickets:
        if ticket[0] not in ways:
            ways[ticket[0]] = [ticket[1]]
            visited[ticket[0]] = [0]
        else:
            ways[ticket[0]].append(ticket[1])
            visited[ticket[0]].append(0)
        if ticket[1] not in ways:
            ways[ticket[1]] = []
            visited[ticket[1]] = []
    for val in ways.values():
        val.sort()
    
    length = len(tickets)
    dfs("ICN", ["ICN"], length)
    return answer[0]

def dfs(start, path, length):
    if len(path) == length + 1:
        answer.append(path)
        print(path)
        return 
    
    if len(answer) > 0:
        return 
    
    for i in range(len(ways[start])):
        if visited[start][i] == 0:
            visited[start][i] = 1
            dfs(ways[start][i], path + [ways[start][i]], length)
            visited[start][i] = 0
            
    
"""
WOW - DFS
from collections import deque

def solution(tickets):
    ways = {}
    for ticket in tickets:
        if ticket[0] not in ways:
            ways[ticket[0]] = [ticket[1]]
        else:
            ways[ticket[0]].append(ticket[1])
        if ticket[1] not in ways:
            ways[ticket[1]] = []
    for val in ways.values():
        val.sort()
    
    answer = []
    dfs(ways, answer, "ICN")
    answer = answer[::-1]
    return answer

def dfs(ways, result, start):
    while ways[start]:
        dfs(ways, result, ways[start].pop(0))
    
    if not ways[start]:
        result.append(start)
        return 
    
"""
    
"""
WOW - DFS
from collections import deque

def solution(tickets):
    ways = {}
    for ticket in tickets:
        if ticket[0] not in ways:
            ways[ticket[0]] = [ticket[1]]
        else:
            ways[ticket[0]].append(ticket[1])
        if ticket[1] not in ways:
            ways[ticket[1]] = []
    for val in ways.values():
        val.sort()
    
    answer = []
    dfs(ways, answer, "ICN")
    answer = answer[::-1]
    return answer

def dfs(ways, result, start):
    while ways[start]:
        dfs(ways, result, ways[start].pop(0))
    
    if not ways[start]:
        result.append(start)
        return 
    
"""
