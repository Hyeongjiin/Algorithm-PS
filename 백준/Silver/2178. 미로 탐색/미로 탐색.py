import sys
from collections import deque

def bfs(place, x, y):
  q = deque([(x, y)])
  while q:
    position = q.popleft()
    x = position[0]
    y = position[1]
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if place[nx][ny] == 0:
        continue
      if place[nx][ny] == 1:
        place[nx][ny] = place[x][y] + 1
        q.append((nx, ny))

N, M = map(int, input().split())
place = []
for i in range(N):
  place.append(list(map(int, input())))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
bfs(place, 0, 0)
print(place[N - 1][M - 1])