from collections import deque
import sys

def bfs(graph, visited, R):
  q = deque([R])
  count = 1
  visited[R] = count
  count += 1
  while q:
    current = q.popleft()
    for i in graph[current]:
      if visited[i] == 0:
        visited[i] = count
        count += 1
        q.append(i)

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(1, N + 1):
  graph[i].sort(reverse = True)

visited = [0] * (N + 1)
bfs(graph, visited, R)

for i in range(1, N + 1):
  print(visited[i])