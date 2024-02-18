from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y, mark):
  q = deque()
  q.append((x, y))
  data[x][y] = mark
  count = 1
  while q:
    cur_x, cur_y = q.popleft()
    for move in moves:
      nx = cur_x + move[0]
      ny = cur_y + move[1]
      if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
        continue
      if data[nx][ny] == 0:
        data[nx][ny] = mark
        count += 1
        q.append((nx, ny))
    
  return count

def cal(x, y):
  result = 0
  kind = set()
  for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
      continue
    if data[nx][ny] == 1:
      continue
    kind.add(data[nx][ny])
  for i in kind:
    result += record[i]
  return result + 1
  
N, M = map(int, input().split())
data = []
for _ in range(N):
  data.append(list(map(int, input().rstrip())))

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
record = {}
count = 2

for i in range(N):
  for j in range(M):
    if data[i][j] == 0:
      result = bfs(i, j, count)
      record[count] = result
      count += 1

for i in range(N):
  for j in range(M):
    if data[i][j] == 1:
      print(cal(i, j) % 10, end="")
    else:
      print(0, end="")
  print()