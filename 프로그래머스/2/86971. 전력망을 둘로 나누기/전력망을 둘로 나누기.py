from collections import deque

def solution(n, wires):
    answer = -1
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    min_diff = 100000000
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j in graph[i]:
                visited = [False] * (n + 1)
                graph[i].remove(j)
                graph[j].remove(i)
                countF = bfs(i, graph, visited)
                countS = bfs(j, graph, visited)
                min_diff = min(min_diff, abs(countF - countS))
                graph[i].append(j)
                graph[j].append(i)
    answer = min_diff
    return answer

def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    count = 0
    while q:
        cur = q.popleft()
        count += 1
        for i in graph[cur]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
    return count