from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for i in range(M):
  a, b = map(int, input().split())
  indegree[b] += 1
  graph[a].append(b)

q = deque()
result = []
for i in range(1, N + 1):
  if indegree[i] == 0:
    q.append(i)
    result.append(i)

while q:
  cur_node = q.popleft()
  for nxt_node in graph[cur_node]:
    indegree[nxt_node] -= 1
    if indegree[nxt_node] == 0:
      q.append(nxt_node)
      result.append(nxt_node)

print(*result)