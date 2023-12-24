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
    for adjN, adjD in cities[now]:
      cost = dist + adjD
      if cost < distance[adjN]:
        distance[adjN] = cost
        prev[adjN] = now
        heapq.heappush(q, (cost, adjN))

N = int(input())
M = int(input())
cities = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
prev = [0] * (N + 1)
for i in range(M):
  start, end, weight = map(int, input().split())
  cities[start].append((end, weight))
start, end = map(int, input().split())
dijkstra(start)

path = [end]
now = end
while now != start:
  now = prev[now]
  path.append(now)

path.reverse()
print(distance[end])
print(len(path))
print(' '.join(map(str, path)))