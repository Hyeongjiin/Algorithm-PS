from collections import deque
import sys

def bfs(ground, x, y):
  q = deque([(x, y)])
  ground[x][y] = -1
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if ground[nx][ny] == 1:
        ground[nx][ny] = -1
        q.append((nx, ny))
    
input = sys.stdin.readline

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  ground = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    ground[y][x] = 1
  result = 0
  for i in range(N):
    for j in range(M):
      if ground[i][j] == 1:
        bfs(ground, i, j)
        result += 1
  print(result)