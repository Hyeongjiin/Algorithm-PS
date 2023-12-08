from collections import deque
import sys

def bfs(houses, x, y):
  result  = 0
  q = deque([(x, y)])
  houses[x][y] = -1
  while q:
    current = q.popleft()
    x = current[0]
    y = current[1]
    result += 1
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
        continue
      if houses[nx][ny] == 1:
        houses[nx][ny] = -1
        q.append((nx, ny))
  return result
  
input = sys.stdin.readline
N = int(input())
houses = []
for i in range(N):
  houses.append(list(map(int, input().rstrip())))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
counts = []

for i in range(N):
  for j in range(N):
    if houses[i][j] == 1:
      counts.append(bfs(houses, i, j))

print(len(counts))
counts.sort()
for count in counts:
  print(count)