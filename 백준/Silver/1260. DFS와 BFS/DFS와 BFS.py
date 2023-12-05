from collections import deque
import sys

input = sys.stdin.readline


def dfs(graph, v, visited, result):
  visited[v] = True
  result.append(str(v))
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited, result)


def bfs(graph, v, visited, result):
  q = deque()
  q.append(v)
  visited[v] = True
  while q:
    v = q.popleft()
    result.append(str(v))
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
  return result


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(N + 1):
  graph[i].sort()

result = []
visited = [False] * (N + 1)
dfs(graph, V, visited, result)
print((' ').join(result))

result = []
visited = [False] * (N + 1)
result = bfs(graph, V, visited, result)
print((' ').join(result))