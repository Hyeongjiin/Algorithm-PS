from collections import deque
import sys

def bfs(earth, i, j):
  q = deque([(i, j)])
  earth[i][j] = -1
  moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1:
        continue
      if earth[nx][ny] == 1:
        earth[nx][ny] = -1
        q.append((nx, ny))

input = sys.stdin.readline

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  earth = []
  for i in range(h):
    earth.append(list(map(int, input().split())))
  island = 0
  for i in range(h):
    for j in range(w):
      if earth[i][j] == 1:
        bfs(earth, i, j)
        island += 1
  print(island)