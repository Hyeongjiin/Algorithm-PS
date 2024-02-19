import sys

input = sys.stdin.readline
INF = int(1e9)

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  graph = [[INF] * (N + 1) for _ in range(N + 1)]
  for i in range(1, N + 1):
    graph[i][i] = 0

  for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u][v] = cost
    graph[v][u] = cost

  for k in range(1, N + 1):
    for i in range(1, N + 1):
      for j in range(1, N + 1):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

  K = int(input())
  friends = list(map(int, input().split()))
  distance = [0] * (N + 1)
  for friend in friends:
    for i in range(1, N + 1):
      distance[i] += graph[friend][i]

  min_val = INF
  min_idx = INF

  for i in range(1, N + 1):
    if distance[i] < min_val:
      min_val = distance[i]
      min_idx = i

  print(min_idx)