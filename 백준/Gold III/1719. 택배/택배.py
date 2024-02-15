import heapq
import sys


def dijkstra(start):
  pq = []
  heapq.heappush(pq, (0, start))
  distance[start] = 0
  path[start] = start
  while pq:
    cur_cost, cur_node = heapq.heappop(pq)
    if cur_cost > distance[cur_node]:
      continue
    for cost, nxt_node in graph[cur_node]:
      nxt_cost = cur_cost + cost
      if nxt_cost < distance[nxt_node]:
        distance[nxt_node] = nxt_cost
        if cur_node == start:
          path[nxt_node] = nxt_node
        else:
          path[nxt_node] = path[cur_node]
        heapq.heappush(pq, (nxt_cost, nxt_node))


input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, cost = map(int, input().split())
  graph[u].append((cost, v))
  graph[v].append((cost, u))

for i in range(1, N + 1):
  distance = [INF] * (N + 1)
  path = [-1] * (N + 1)
  dijkstra(i)
  for j in range(1, N + 1):
    if j == i:
      print('-', end=' ')
    else:
      print(path[j], end=' ')
  print()