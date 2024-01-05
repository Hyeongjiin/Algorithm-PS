from collections import deque
import sys

input = sys.stdin.readline


def airPollution(cheese, air):
  q = deque()
  q.append((0, 0))
  air[0][0] = True
  while q:
    x, y = q.popleft()
    for move in moves:
      nx = x + move[0]
      ny = y + move[1]
      if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
        continue
      if cheese[nx][ny] == 0 and air[nx][ny] == False:
        air[nx][ny] = True
        q.append((nx, ny))


N, M = map(int, input().split())
cheese = []
for i in range(N):
  cheese.append(list(map(int, input().rstrip().split())))

time = 0
total = N * M
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while True:
  air = [[False] * M for _ in range(N)]
  airPollution(cheese, air)
  count = 0
  for i in range(N):
    for j in range(M):
      if air[i][j] == True:
        count += 1
      cheeseCount = 0
      if cheese[i][j] == 1:
        for move in moves:
          ni = i + move[0]
          nj = j + move[1]
          if ni < 0 or nj < 0 or ni > N - 1 or nj > M - 1:
            continue
          if air[ni][nj] == True:
            cheeseCount += 1
        if cheeseCount >= 2:
          cheese[i][j] = 0
  if count == N * M:
    break
  time += 1

print(time)
