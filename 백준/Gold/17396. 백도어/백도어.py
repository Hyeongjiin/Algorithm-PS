import heapq
import sys

input = sys.stdin.readline
INF = 100000 * 100000 + 1

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for adjN, adjD in graph[now]:
      if sight[adjN] == 1:
        continue
      cost = dist + adjD
      if cost < distance[adjN]:
        distance[adjN] = cost
        heapq.heappush(q, (cost, adjN))


N, M = map(int, input().split())
sight = list(map(int, input().split()))
sight[N - 1] = 0
graph = [[] for _ in range(N)]
distance = [INF] * N
for i in range(M):
  start, end, time = map(int, input().split())
  graph[start].append((end, time))
  graph[end].append((start, time))
dijkstra(0)

if distance[N - 1] == INF:
  print(-1)
else:
  print(distance[N - 1])