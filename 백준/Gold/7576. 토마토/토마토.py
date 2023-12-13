from collections import deque
import sys

def bfs():
  q = deque()
  cnt = 0
  maxi = 0
  for i in range(N):
    for j in range(M):
      if tomatoes[i][j] == 1:
        q.append((i, j))
      elif tomatoes[i][j] == 0:
        cnt += 1
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    day = tomatoes[x][y]
    if maxi < day:
      maxi = day
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if tomatoes[nx][ny] == 0:
        cnt -= 1
        tomatoes[nx][ny] = day + 1
        q.append((nx, ny))
  if cnt == 0:
    return True, maxi - 1
  else:
    return False, - 1

input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = []
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(N):
  tomatoes.append(list(map(int, input().split())))

result, maxi = bfs()

if result == True:
  print(maxi)
else:
  print(maxi)