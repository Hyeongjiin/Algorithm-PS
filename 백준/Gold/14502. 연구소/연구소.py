from collections import deque
import sys

def bfs(lab, x, y, visited):
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
      if lab[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append((nx, ny))

def solve(lab, visited):
  for i in range(N):
    for j in range(M):
      if lab[i][j] == 2:
        bfs(lab, i, j, visited)
  result = 0
  for i in range(N):
    for j in range(M):
      if lab[i][j] == 0 and visited[i][j] == False:
        result += 1
  return result

input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
for i in range(N):
  lab.append(list(map(int, input().split())))

positions = []
for i in range(N):
  for j in range(M):
    if lab[i][j] == 0:
      positions.append((i, j))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

length = len(positions)
maxi = 0
for i in range(length - 2):
  for j in range(i + 1, length - 1):
    for k in range(j + 1, length):
      lab[positions[i][0]][positions[i][1]] = 1
      lab[positions[j][0]][positions[j][1]] = 1
      lab[positions[k][0]][positions[k][1]] = 1
      visited = [[False] * M for _ in range(N)]
      maxi = max(maxi, solve(lab, visited))
      lab[positions[i][0]][positions[i][1]] = 0
      lab[positions[j][0]][positions[j][1]] = 0
      lab[positions[k][0]][positions[k][1]] = 0

print(maxi)