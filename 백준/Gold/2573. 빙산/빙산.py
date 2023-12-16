from collections import deque
import sys

def melt(ice, x, y):
  q = deque([(x, y)])
  melt = deque()
  visited = [[False] * M for _ in range(N)]
  visited[x][y] = True
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    count = 0
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if ice[nx][ny] == 0:
        count += 1
      if ice[nx][ny] > 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append((nx, ny))
    melt.append((x, y, count))
  while melt:
    current = melt.popleft()
    x = current[0]
    y = current[1]
    c = current[2]
    ice[x][y] -= c
    if ice[x][y] < 0:
      ice[x][y] = 0

def bfs(ice, visited, x, y):
  q = deque([(x, y)])
  visited[x][y] = True
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if ice[nx][ny] > 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append((nx, ny))

input = sys.stdin.readline

N, M = map(int, input().split())
ice = []
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(N):
  ice.append(list(map(int, input().split())))

result = 0

while True:
  count = 0
  visited = [[False] * M for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if ice[i][j] > 0 and visited[i][j] == False:
        bfs(ice, visited, i, j)
        count += 1
  if count > 1:
    break
  if count == 0:
    result = 0
    break
  flag = 0
  for i in range(N):
    if flag == 1:
      break
    for j in range(M):
      if ice[i][j] > 0:
        melt(ice, i, j)
        flag = 1
        result += 1
        break

print(result)