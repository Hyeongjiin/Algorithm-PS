import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x, y):
  pq = []
  heapq.heappush(pq, (0, x, y))
  distance[x][y] = 0
  visited[x][y] = True
  while pq:
    cur_cost, cur_x, cur_y = heapq.heappop(pq)
    if cur_x == N - 1 and cur_y == M - 1:
      break
    for move in moves:
      nx = cur_x + move[0]
      ny = cur_y + move[1]
      if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
        continue
      if visited[nx][ny] == True:
        continue
      nxt_cost = INF
      if room[nx][ny] == '0':
        nxt_cost = cur_cost
      elif room[nx][ny] == '1':
        nxt_cost = cur_cost + 1
      distance[nx][ny] = nxt_cost
      visited[nx][ny] = True 
      heapq.heappush(pq, (nxt_cost, nx, ny))


M, N = map(int, input().split())
room = []
for i in range(N):
  room.append(list(input().rstrip()))
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

distance = [[INF] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dijkstra(0, 0)
print(distance[N - 1][M - 1])