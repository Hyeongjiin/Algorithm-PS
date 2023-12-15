from collections import deque
import sys

def bfs(ground, visited, h, i, j):
  q = deque([(i, j)])
  visited[i][j] = True
  moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
        continue
      if ground[nx][ny] > h and visited[nx][ny] == False:
        visited[nx][ny] = True
        q.append((nx, ny))

input = sys.stdin.readline

N = int(input())
ground = []
maxi = 0
for i in range(N):
  ground.append(list(map(int, input().split())))
  for j in ground[i]:
    maxi = max(maxi, j)

safe_max = 0
for i in range(maxi):
  count = 0
  visited = [[False] * N for _ in range(N)]
  for j in range(N):
    for k in range(N):
      if ground[j][k] > i and visited[j][k] == False:
        bfs(ground, visited, i, j, k)
        count += 1
  safe_max = max(safe_max, count)
print(safe_max)