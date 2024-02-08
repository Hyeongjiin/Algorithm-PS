from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    visited[1] = -1
    for vertex in edge:
        graph[vertex[0]].append(vertex[1])
        graph[vertex[1]].append(vertex[0])
    bfs(1, graph, visited)
    answer = visited.count(max(visited))
    return answer

def bfs(start, graph, visited):
    q = deque()
    count = 0
    q.append((start, count))
    while q:
        cur_node, cur_count = q.popleft()
        for nxt_node in graph[cur_node]:
            if visited[nxt_node] == 0:
                visited[nxt_node] = cur_count + 1
                q.append((nxt_node, cur_count + 1))
                
    
    
    