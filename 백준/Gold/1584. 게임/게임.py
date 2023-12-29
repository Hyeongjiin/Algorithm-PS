from collections import deque
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(grid, distance):
  q = []
  heapq.heappush(q, (0, 0, 0))
  distance[0][0] = 0
  moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  while q:
    cost, x, y = heapq.heappop(q)
    if distance[x][y] < cost:
      continue
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > 500 or ny > 500:
        continue
      if grid[nx][ny] < 2:
        ncost = cost + grid[nx][ny]
        if ncost < distance[nx][ny]:
          distance[nx][ny] = ncost
          heapq.heappush(q, (ncost, nx, ny))


def bfs(grid, visited):
  q = deque()
  q.append((0, 0, 0))
  visited[0][0] = True
  moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  result = -1
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    cost = current[2]
    if x == 500 and y == 500:
      result = cost
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > 500 or ny > 500:
        continue
      if visited[nx][ny] == False and grid[nx][ny] < 2:
        visited[nx][ny] = True
        ncost = cost + grid[nx][ny]
        q.append((nx, ny, ncost))

  return result


grid = [[0] * 501 for _ in range(501)]
#visited = [[False] * 501 for _ in range(501)]
distance = [[INF] * 501 for _ in range(501)]
N = int(input())
if N > 0:
  for i in range(N):
    danger = list(map(int, input().split()))
    X1 = min(danger[0], danger[2])
    X2 = max(danger[0], danger[2])
    Y1 = min(danger[1], danger[3])
    Y2 = max(danger[1], danger[3])
    for i in range(X1, X2 + 1):
      for j in range(Y1, Y2 + 1):
        grid[i][j] = 1
M = int(input())
if M > 0:
  for i in range(M):
    death = list(map(int, input().split()))
    X1 = min(death[0], death[2])
    X2 = max(death[0], death[2])
    Y1 = min(death[1], death[3])
    Y2 = max(death[1], death[3])
    for i in range(X1, X2 + 1):
      for j in range(Y1, Y2 + 1):
        grid[i][j] = 2
#print(bfs(grid, visited))
dijkstra(grid, distance)
if distance[500][500] == INF:
  print(-1)
else:
  print(distance[500][500])