from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in graph:
  i.sort()

count = 1
visited = [0] * (N + 1)
visited[R] = count
q = deque()
q.append((R, count))
while q:
  cur_node, cur_count = q.popleft()
  for nxt_node in graph[cur_node]:
    if visited[nxt_node] == 0:
      count += 1
      q.append((nxt_node, count))
      visited[nxt_node] = count

for i in range(1, N + 1):
  print(visited[i])