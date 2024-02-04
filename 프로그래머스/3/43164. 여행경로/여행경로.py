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
