import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
  start, end = map(int, input().split())
  graph[start].append(end)
  indegree[end] += 1

q = []
for i in range(1, N + 1):
  if indegree[i] == 0:
    q.append(i)

result = []
while q:
  cur_node = heapq.heappop(q)
  result.append(cur_node)
  for nxt_node in graph[cur_node]:
    indegree[nxt_node] -= 1
    if indegree[nxt_node] == 0:
      heapq.heappush(q, nxt_node)

print(*result)