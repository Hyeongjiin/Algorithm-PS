from collections import deque
import sys

def bfs(graph, visited, start):
  q = deque([start])
  visited[start] = True
  while q:
    current = q.popleft()
    for i in graph[current]:
      if visited[i] == False:
        visited[i] = True
        q.append(i)

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] * M for _ in range(N + 1)]
for i in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

visited = [False] * (N + 1)
component = 0
for i in range(1, N + 1):
  if visited[i] == False:
    bfs(graph, visited, i)
    component += 1

print(component)