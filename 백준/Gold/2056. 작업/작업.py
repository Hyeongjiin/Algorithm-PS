from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
time = [0] * (N + 1)
result = [0] * (N + 1)

for idx in range(N):
  data = list(map(int, input().split()))
  time[idx + 1] = data[0]
  indegree[idx + 1] = data[1]
  if data[1] != 0:
    for i in range(2, len(data)):
      graph[data[i]].append(idx + 1)

q = deque()
for i in range(1, N + 1):
  if indegree[i] == 0:
    result[i] = time[i]
    q.append(i)

while q:
  cur_node = q.popleft()
  for nxt_node in graph[cur_node]:
    indegree[nxt_node] -= 1
    result[nxt_node] = max(result[nxt_node], time[nxt_node] + result[cur_node])
    if indegree[nxt_node] == 0:
      q.append(nxt_node)

print(max(result))