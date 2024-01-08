from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
times = [0] * (N + 1)
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

for i in range(N):
  data = list(map(int, input().split()))
  times[i + 1] = data[0]
  indegree[i + 1] = len(data) - 2
  for j in range(1, len(data) - 1):
    graph[data[j]].append(i + 1)

for i in range(1, N + 1):
  result[i] = times[i]

q = deque()
for i in range(1, N + 1):
  if indegree[i] == 0:
    q.append(i)

while q:
  cur_node = q.popleft()
  for nxt_node in graph[cur_node]:
    indegree[nxt_node] -= 1
    result[nxt_node] = max(result[nxt_node], result[cur_node] + times[nxt_node])
    if indegree[nxt_node] == 0:
      q.append(nxt_node)

for i in range(1, N + 1):
  print(result[i])