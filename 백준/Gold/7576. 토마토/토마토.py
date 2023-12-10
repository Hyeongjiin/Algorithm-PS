from collections import deque
import sys

def bfs(tomatoes, visited):
  day = 0
  q = deque()
  for i in range(N):
    for j in range(M):
      if tomatoes[i][j] == 1:
        q.append((i, j, day))
        visited[i][j] = True
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    day = current[2]
    day += 1
    tomatoes[x][y] = day
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if tomatoes[nx][ny] == -1 or tomatoes[nx][ny] == 1:
        continue
      if tomatoes[nx][ny] >= 2 and tomatoes[nx][ny] < day:
        continue
      if visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append((nx, ny, day))

input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = []
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(N):
  tomatoes.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
bfs(tomatoes, visited)

result = False
maxi = 0

for i in range(N):
  for j in range(M):
    if tomatoes[i][j] == 0:
      result = True
    maxi = max(maxi, tomatoes[i][j])
    
if result == True:
  print(-1)
else:
  print(maxi - 1)