from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
result = []

for i in range(M):
  data = list(map(int, input().split()))
  for j in range(2, data[0] + 1):
    graph[data[j - 1]].append(data[j])
    indegree[data[j]] += 1

q = deque()
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

if len(result) == N:
  for i in range(N):
    print(result[i])
else:
  print(0)
