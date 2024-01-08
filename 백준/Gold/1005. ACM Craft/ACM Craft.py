from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  graph = [[] for _ in range(N + 1)]
  indegree = [0] * (N + 1)
  times = [0] * (N + 1)
  result = [0] * (N + 1)
  data = list(map(int, input().split()))
  for i in range(N):
    times[i + 1] = data[i]
    result[i + 1] = data[i]
  for i in range(K):
    start, end = map(int, input().split())
    indegree[end] += 1
    graph[start].append(end)
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
  W = int(input())
  print(result[W])