import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for adjN, adjD in coms[now]:
      cost = dist + adjD
      if cost < distance[adjN]:
        distance[adjN] = cost
        heapq.heappush(q, (cost, adjN))


T = int(input())
for i in range(T):
  N, D, C = map(int, input().split())
  distance = [INF] * (N + 1)
  coms = [[] for _ in range(N + 1)]
  for j in range(D):
    end, start, time = map(int, input().split())
    coms[start].append((end, time))
  dijkstra(C)
  count = 0
  result = 0
  for j in distance:
    if j < INF:
      count += 1
      result = max(result, j)
  print(count, result)