from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
  q = deque()
  q.append((x, y))
  distance[x][y] = 0
  visited[x][y] = True
  while q:
    cur_x, cur_y = q.popleft()
    for move in moves:
      nx = cur_x + move[0]
      ny = cur_y + move[1]
      if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
        continue
      if visited[nx][ny] == True:
        continue
      if distance[nx][ny] == 0:
        continue
      distance[nx][ny] = distance[cur_x][cur_y] + 1
      visited[nx][ny] = True
      q.append((nx, ny))

N, M = map(int, input().split())
distance = []
for _ in range(N):
  distance.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]

x = -1
y = -1
for i in range(N):
  for j in range(M):
    if distance[i][j] == 2:
      x = i
      y = j

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bfs(x, y)

for i in range(N):
  for j in range(M):
    if visited[i][j] == False and distance[i][j] == 1:
      distance[i][j] = -1

for i in distance:
  print(*i)