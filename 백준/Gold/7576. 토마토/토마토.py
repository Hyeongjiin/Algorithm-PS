from collections import deque
import sys

def bfs():
  day = 0
  q = deque()
  cnt = 0
  maxi = 0
  for i in range(N):
    for j in range(M):
      if tomatoes[i][j] == 1:
        q.append((i, j, day))
        visited[i][j] = True
      elif tomatoes[i][j] == 0:
        cnt += 1
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    day = current[2]
    day += 1
    tomatoes[x][y] = day
    if maxi < day:
      maxi = day
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if visited[nx][ny] == False and tomatoes[nx][ny] == 0:
        cnt -= 1
        visited[nx][ny] = True
        q.append((nx, ny, day))
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

visited = [[False] * M for _ in range(N)]
result, maxi = bfs()

if result == True:
  print(maxi)
else:
  print(maxi)