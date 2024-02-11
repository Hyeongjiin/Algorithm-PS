from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y, color):
  count = 1
  q = deque()
  q.append((x, y))
  while q:
    cur_x, cur_y = q.popleft()
    for move in moves:
      nx = cur_x + move[0]
      ny = cur_y + move[1]
      if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1:
        continue
      if war[nx][ny] == color and visited[nx][ny] == False:
        count += 1
        q.append((nx, ny))
        visited[nx][ny] = True
  return count


N, M = map(int, input().split())
war = []
for i in range(M):
  war.append(list(input().rstrip()))

visited = [[False] * N for _ in range(M)]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

powerW = 0
powerB = 0

for i in range(M):
  for j in range(N):
    if visited[i][j] == False:
      visited[i][j] = True
      result = bfs(i, j, war[i][j])
      if war[i][j] == 'W':
        powerW += result ** 2
      elif war[i][j] == 'B':
        powerB += result ** 2

print(powerW, powerB)